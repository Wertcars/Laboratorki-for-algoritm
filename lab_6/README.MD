# Description of lab

This lab demonstrates the fundamentals of Python’s object model and how custom classes integrate with the language.
The main goal is to implement a Student class and gradually extend its behavior using special (dunder) methods and type annotations.

The lab consists of tasks A–G where each task focuses on a specific aspect of object-oriented programming and type safety.

## Requirement

- Python 3.10+
- Windows/Linux/macOS

## Installing

### 1. Create a virtual environment
It is recommended to create a virtual environment to isolate dependencies:

```
cd lab_6
python -m venv .venv
```
### Activate it:

On Windows:
```
.venv\Scripts\activate
```
On Linux/macOS:
```
source .venv/bin/activate
```

### Install dependencies:

```
pip install -r requirements.txt
```

## Command to Run the Program

```bash
python src/lab6.py
```
## Type Checking

``` bash
mypy --strict src/
```

## Project Structure

```
lab_6/ 
│ 
├─ README.md 
├─ requirements.txt 
│ 
├─ src/ 
│   │─ lab6.py
│   └─ Student.py
│ 
└─ report/ 
    └─ answers.md 
```

## Description of program

The program prints several structured sections (A–H), each focused on a specific concept of working with classes and objects in Python:

- Define the Student Class  
  Creates a class with attributes (`name`, `group`, `average_grade`)  
  Prints the values of object from class

- Inspect Internal Structure  
  Prints the internal dictionary (`__dict__`) of an object and shows how modifying it affects the object

- String Representation (`__str__`)  
  Prints a human-readable description of the object

- Developer Representation (`__repr__`)  
  Prints a formal representation useful for debugging

- Equality (`__eq__`)  
  Prints results of comparisons between objects using `==`, including comparisons with unrelated types

- Ordering (`__lt__`)  
  Prints results of comparisons using `<` and demonstrates error handling for invalid comparisons

- Sorting  
  Prints a sorted list of `Student` objects using built-in sorting, relying on the implemented comparison logic

The output is structured to clearly demonstrate how Python objects store data, how special methods control behavior, and how type hints help create clean and safe code.
