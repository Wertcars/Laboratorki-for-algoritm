import pytest

from src.async_tool.models import TaskItem
from src.async_tool.processor import process_item


@pytest.mark.asyncio
async def test_process_item_success() -> None:
    item: TaskItem = {
        "id": 1,
        "delay": 0.01,
        "good": True,
    }

    result = await process_item(item)

    assert result == {
        "id": 1,
        "status": "done",
    }


@pytest.mark.asyncio
async def test_process_item_failure() -> None:
    item: TaskItem = {
        "id": 2,
        "delay": 0.01,
        "good": False,
    }

    with pytest.raises(ValueError, match="Task 2 failed"):
        await process_item(item)


@pytest.mark.asyncio
async def test_process_item_structure() -> None:
    item: TaskItem = {
        "id": 3,
        "delay": 0.01,
        "good": True,
    }

    result = await process_item(item)

    assert isinstance(result, dict)
    assert "id" in result
    assert "status" in result
    assert result["status"] == "done"