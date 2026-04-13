## 1. What is duck typing?

Duck typing is an approach in Python where an object's type is determined by its behavior, not by its class or inheritance.

If an object has the required methods, it can be used.

Example:

```
def export(obj):
    print(obj.serialize())
```

Any object with a serialize() method will work, even if it does not inherit from any specific class.

Focuses on behavior, not type  
No inheritance required

Limitation:
Errors occur only at runtime if a required method is missing.

## 2. How does Protocol differ from ABC?

Protocol and ABC (Abstract Base Class) both define interfaces, but in different ways.

Protocol uses structural typing
ABC uses nominal typing (inheritance)

Key differences:

Protocol:
No inheritance required
Checked by tools like mypy
More flexible
ABC:
Requires inheritance
Enforced at runtime
More strict

## 3. Does Protocol require inheritance? Why or why not?

No, Protocol does not require inheritance.

This is because it uses structural typing — it checks whether an object has the required methods.

Example:

```
class Student:
    def serialize(self) -> str:
        return "data"
```

Even without inheriting from Protocol, this class satisfies it because it implements serialize().

Why it works:
Python checks the structure (methods), not the class hierarchy.

## 4. What problem does ABC solve?

ABC (Abstract Base Class) ensures that subclasses implement required methods.

Example:

```
from abc import ABC, abstractmethod

class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass
```

If a subclass does not implement serialize(), it cannot be instantiated.

What problem it solves:

Prevents creating incomplete classes
Enforces a strict interface
Makes code more predictable

## 5. What does @dataclass generate automatically?

The @dataclass decorator automatically generates common methods for a class.

It creates:

- ```__init__()``` - constructor  
- ```__repr__()``` - string representation  
- ```__eq__()``` - comparison  

Example:

```
@dataclass
class Student:
    name: str
    group: str
    average_grade: float
```

This reduces boilerplate code and makes classes easier to write.

## 6. What changes when using slots?

Using slots (e.g., ```@dataclass(slots=True)```) changes how object attributes are stored.

Key effects:

No ```__dict__``` is created
Fixed set of attributes
Cannot add new attributes dynamically

Example:

```
student.new_field = "test"  # Error
```

Advantages:

Lower memory usage
Faster attribute access

Limitations:

Less flexible (cannot add new fields)

## 7. Why does Protocol work with different implementations (regular class, dataclass, slots)?

Protocol works because it relies on structural typing.

It only checks whether an object has the required method:

```
def serialize(self) -> str
```

It does not matter how the class is implemented:

- Regular class -> works  
- Dataclass -> works  
- Slots -> works  

Reason:

All these classes implement the same method (serialize()), so they match the Protocol.