# Description of lab

This lab demonstrates how core Python protocols define object behavior and how custom classes can integrate with built-in language features.

The main goal is to implement a student management system that supports iteration, context management, and controlled attribute access.

The lab consists of tasks A–D where each task focuses on a specific Python protocol:

- iteration protocol (`__iter__`, `__next__`)
- context manager protocol (`__enter__`, `__exit__`)
- descriptor protocol (`__get__`, `__set__`, `__set_name__`)

The purpose of this lab is to show that Python behavior is driven by special methods rather than inheritance.

---

## Requirement

- Python 3.10+
- Windows/Linux/macOS

## Installing

### 1. Create a virtual environment
It is recommended to create a virtual environment to isolate dependencies:

```
cd lab_8
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
python src/lab8.py
```
## Type Checking

``` bash
mypy --strict src/
```

## Project Structure

```
lab_8/ 
│ 
├─ README.md 
├─ requirements.txt 
│ 
├─ src/ 
│   │─ lab8.py
│   └─ Students.py
│ 
└─ report/ 
    └─ answers.md 
```

## Description of program

The program prints several structured sections (Task A–D), each demonstrating a different Python mechanism:

- Task A - Iteration
  Creates a custom collection of students
  Implements an iterator using `__iter__()` and `__next__()`
  Demonstrates that the collection can be used in a `for` loop

- Task B - Context Manager
  Extends the collection to support the `with` statement
  Implements `__enter__()` and `__exit__()`
  Shows messages when entering and exiting the context
  Demonstrates that `__exit__()` is called even if an error occurs

- Task C - Descriptor
  Implements a descriptor to validate student grades
  Restricts values to a valid range (0–100)
  Demonstrates controlled attribute access and error handling

- Task D - Integration
  Combines iteration, context manager, and descriptor
  Uses all components together in a single workflow
  Demonstrates how multiple Python protocols interact

