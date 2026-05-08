import asyncio
import logging

from async_tool.models import TaskItem, TaskResult

logger = logging.getLogger(__name__)


async def process_item(item: TaskItem) -> TaskResult:
    await asyncio.sleep(item["delay"])

    if not item["good"]:
        raise ValueError(f"Task {item['id']} failed")

    return {
        "id": item["id"],
        "status": "done",
    }


async def safe_process_item(
    item: TaskItem,
    continue_on_error: bool,
) -> TaskResult:
    logger.info("Starting task %s", item["id"])

    try:
        result = await process_item(item)
        logger.info("Completed task %s", item["id"])
        return result

    except Exception as error:
        logger.error(
            "Task %s failed: %s",
            item["id"],
            error,
        )

        if not continue_on_error:
            raise

        return {
            "id": item["id"],
            "status": "error",
            "message": str(error),
        }


async def run_sync(
    items: list[TaskItem],
    continue_on_error: bool,
) -> list[TaskResult]:
    results: list[TaskResult] = []

    for item in items:
        result = await safe_process_item(
            item,
            continue_on_error,
        )
        results.append(result)

    return results


async def run_async(
    items: list[TaskItem],
    continue_on_error: bool,
) -> list[TaskResult]:
    tasks = [
        safe_process_item(item, continue_on_error)
        for item in items
    ]

    return await asyncio.gather(*tasks)


async def run_limited(
    items: list[TaskItem],
    limit: int,
    continue_on_error: bool,
) -> list[TaskResult]:
    semaphore = asyncio.Semaphore(limit)

    async def worker(item: TaskItem) -> TaskResult:
        async with semaphore:
            return await safe_process_item(
                item,
                continue_on_error,
            )

    tasks = [worker(item) for item in items]

    return await asyncio.gather(*tasks)
