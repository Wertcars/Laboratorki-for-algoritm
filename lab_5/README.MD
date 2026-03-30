# Description of lab

This lab demonstrates the use of type hints in Python, including typed functions, collections, generics, function types, and static type checking with mypy.
The program consists of seven independent tasks (A–G). Each task explores a specific concept of typing and functional programming using clear examples and printed output.

## Requirement

- Python 3.10+
- Windows/Linux/macOS

## Installing

### 1. Create a virtual environment
It is recommended to create a virtual environment to isolate dependencies:

```
cd lab_5
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
pip install -r requirement.txt
```

## Command to Run the Program

```bash
python src/lab5.py
```
## Type Checking

``` bash
mypy --strict src/
```

## Project Structure

```
lab_5/ 
│ 
├─ README.md 
├─ requirements.txt 
│ 
├─ src/ 
│   └─ lab5.py
│ 
└─ report/ 
    └─ answers.md 
```

## Description of program

The program prints several structured sections (A–G), each focused on a specific Python typing concept:

- Basic Type Hints  
  Prints results of functions with annotated parameters and return types, e.g. addition and list squaring
- Typed Collections  
  Prints filtered lists such as even numbers using typed lists
- Optional  
  Prints results of searching values, returning either a value or None
- Function Type (Callable)  
  Prints results of applying different functions passed as arguments
- Generics  
  Prints the first element from lists of different types using a generic type G
- Function Returning Function  
  Prints results of dynamically created functions like multipliers
- Pipeline  
  Prints the result of a processing pipeline: filtering, transforming, and aggregating data

The output is designed to demonstrate how type hints improve code clarity, safety, and structure in Python.