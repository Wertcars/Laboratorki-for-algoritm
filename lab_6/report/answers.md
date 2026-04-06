## 1. What is stored in obj.\_\_dict__?

`obj.__dict__` stores all **instance attributes** of an object in the form of a dictionary.
Keys are attribute names, and values are the corresponding attribute values.

Example:

```python
{'name': 'Ivan', 'group': 'KH-101', 'average_grade': 85.5}
```

---


## 2. What is the difference between a class and an object?

A **class** is a blueprint or template used to create objects.
An **object** is an instance of a class with actual data.

* Class -> defines structure and behavior
* Object -> specific instance with data

---


## 3. What does \_\_init__ do?

`__init__` is a constructor method that is automatically called when an object is created.

It is used to:

* initialize object attributes
* assign initial values to the object

---


## 4. Who calls \_\_str__ and when?

`__str__` is called by Python automatically for any object from class:

* `print(Student)` is used
* `str(Student)` is called

It provides a **human-readable representation** of the object.

---


## 5. What is the difference between == and is?

* `==` compares **values** (uses `__eq__`)
* `is` compares **identity** (whether two variables refer to the same object in memory)

---


## 6. Why do we use other: object in \_\_eq__ and \_\_lt__?

We use `other: object` because:

* these methods must accept **any type**, not only the same class
* it ensures compatibility with Python’s data model
* allows safe type checking using `isinstance()`

This prevents errors and ensures correct behavior when comparing with
unrelated types.
