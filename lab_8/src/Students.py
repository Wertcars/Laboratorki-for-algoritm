from typing import Generic, TypeVar, Iterator, List, Optional, Literal


class GradeDescriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        self.private_name = "_" + name

    def __get__(self, instance: object, owner: type) -> int:
        if instance is None:
            raise AttributeError
        return int(getattr(instance, self.private_name))

    def __set__(self, instance: object, value: int) -> None:
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        setattr(instance, self.private_name, value)


class Student:
    grade = GradeDescriptor()

    def __init__(self, name: str, group: str, grade: int):
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"Student - {self.name}, group - {self.group}, grade = {self.grade}"
    

T = TypeVar("T")

class StudentIterator(Generic[T]):
    def __init__(self, students: List[T]):
        self._students = students
        self._index = 0

    def __iter__(self) -> "StudentIterator[T]":
        return self

    def __next__(self) -> T:
        if self._index >= len(self._students):
            raise StopIteration
        value = self._students[self._index]
        self._index += 1
        return value
    

class StudentCollection:
    def __init__(self, students: List[Student]):
        self._students = students

    def __iter__(self) -> Iterator[Student]:
        return StudentIterator(self._students)
    

class StudentCollectionCM(StudentCollection):
    def __enter__(self) -> "StudentCollectionCM":
        print(">>> Entering context")
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[object],
    ) -> Literal[True]:
        print("<<< Exiting context")
        return True