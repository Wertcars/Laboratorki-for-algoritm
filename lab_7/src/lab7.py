from typing import Protocol
from dataclasses import dataclass
from abc import ABC, abstractmethod

class Serializable(Protocol):
    def serialize(self) -> str: ...

def export(obj: Serializable) -> None:
    print(obj.serialize())


print("Task A - Regular class (duck typing)")
print()

class Student:
    def __init__(self, name: str, group: str, average_grade: float):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"Student(name = {self.name}, group = {self.group}, grade = {self.average_grade})"
    
student_a = Student("Kiril Baltyanko", "KN-125", 60.0)
export(student_a)

print()
print("What do we see: the class works without inheritance")
print("Why: duck typing - it has a serialize() method, so it fits")

print("-------------------------------------------------")


print("Task B - Dataclass implementation")
print()

@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"StudentData(name = {self.name}, group = {self.group}, grade = {self.average_grade})"
    
student_b = StudentData("Nikita Kozlov", "KN-114", 89.4)
export(student_b)

print()
print("What do we see: class StudentData has less code (dataclass)")
print("Why: @dataclass automatically generates __init__ and others")

print("-------------------------------------------------")


print("Task C - Slots")
print()

@dataclass(slots=True)
class StudentSlots:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"StudentSlots(name = {self.name}, group = {self.group}, grade = {self.average_grade})"
    
student_c = StudentSlots("Jhon Kharkovskiy", "KN-123", 100.0)
export(student_c)

print("Attempt to add a new field:")
try:
    student_c.new_field = "test"
except AttributeError as e:
    print("Error:", e)

print()
print("What do we see: cannot add a new attribute")
print("Why: slots fix (restrict) the object structure")

print("-------------------------------------------------")


print("Task D - ABC version")
print()
    
class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"StudentABC(name = {self.name}, group = {self.group}, grade = {self.average_grade})"
    
student_d = StudentABC("Glib Senior", "KN-124", 96.9)
export(student_d)

print()
print("What do we see: works with ABC-based implementation")
print("Why: the class inherits from ABC and implements serialize()")

print("-------------------------------------------------")