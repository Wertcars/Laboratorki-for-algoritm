from typing import TypedDict


class TaskItem(TypedDict):
    id: int
    delay: float
    good: bool


class TaskResult(TypedDict, total=False):
    id: int
    status: str
    message: str
