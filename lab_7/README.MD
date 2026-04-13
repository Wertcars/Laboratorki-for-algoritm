# Description of lab

This lab demonstrates different approaches to defining behavior in Python and how objects can be treated as the same “type” based on their functionality.

The main goal is to implement a serializable object and explore multiple ways to define it using duck typing, Protocols, dataclasses, slots, and Abstract Base Classes (ABC).

The lab consists of tasks A–D where each task focuses on a specific concept of behavior definition, type checking, and interface design in Python.

## Requirement

- Python 3.10+
- Windows/Linux/macOS

## Installing

### 1. Create a virtual environment
It is recommended to create a virtual environment to isolate dependencies:

```
cd lab_7
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
python src/lab7.py
```
## Type Checking

``` bash
mypy --strict src/
```

## Project Structure

```
lab_7/ 
│ 
├─ README.md 
├─ requirements.txt 
│ 
├─ src/ 
│   └─ lab7.py
│ 
└─ report/ 
    └─ answers.md 
```

## Description of program

The program prints several structured sections (Task A–D), each demonstrating a different way to implement a serializable object in Python:

- Task A - Regular class (duck typing)  
  Creates a simple class with attributes (`name`, `group`, `average_grade`)  
  Implements `serialize()` method  
  Demonstrates that the object works without inheritance  

- Task B - Dataclass  
  Uses `@dataclass` to simplify class definition  
  Automatically generates constructor and other methods  
  Shows the same behavior as a regular class with less code  

- Task C - Dataclass with slots  
  Uses `@dataclass(slots=True)`  
  Demonstrates restricted object structure  
  Shows that adding new attributes is not allowed  

- Task D - Abstract Base Class (ABC)    
  Defines an interface using `ABC` and `@abstractmethod`  
  Requires explicit inheritance  
  Ensures that `serialize()` is implemented  

Additionally:

- A Protocol (Serializable) is defined to describe the required behavior  
- A helper function `export()` is used to call `serialize()` on any compatible object  
- The program demonstrates that all implementations work with Protocol due to structural typing  
