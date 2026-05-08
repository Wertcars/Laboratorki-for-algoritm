import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

from async_tool.models import TaskItem, TaskResult
from async_tool.processor import (
    run_async,
    run_limited,
    run_sync,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Async batch processor",
    )

    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to JSON input file",
    )

    parser.add_argument(
        "--mode",
        choices=["sync", "async", "limited"],
        default="sync",
        help="Execution mode",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Concurrency limit for limited mode",
    )

    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue processing after errors",
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="WARNING",
        help="Logging level",
    )

    return parser.parse_args()


def setup_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(levelname)s: %(message)s",
    )


def load_items(path: Path) -> list[TaskItem]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data


async def execute(
    items: list[TaskItem],
    mode: str,
    limit: int,
    continue_on_error: bool,
) -> list[TaskResult]:
    if mode == "sync":
        return await run_sync(
            items,
            continue_on_error,
        )

    if mode == "async":
        return await run_async(
            items,
            continue_on_error,
        )

    return await run_limited(
        items,
        limit,
        continue_on_error,
    )


def main() -> None:
    args = parse_args()

    setup_logging(args.log_level)

    BASE_DIR = Path(__file__).resolve().parents[2]
    input_path = BASE_DIR / args.input_file
    items = load_items(input_path)

    try:
        results = asyncio.run(
            execute(
                items=items,
                mode=args.mode,
                limit=args.limit,
                continue_on_error=args.continue_on_error,
            )
        )

        print(
            json.dumps(
                results,
                indent=2,
            )
        )

    except Exception as error:
        print(
            f"Error: {error}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
