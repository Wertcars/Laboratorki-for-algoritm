# Description of lab

This lab demonstrates higher-order functions, functional transformations using map and filter, and decorators in Python, including decorators with arguments and caching.
The program consists of six independent tasks (A–G).

## Requirement

- Python 3.10+
- Windows/Linux/macOS

## Command to Run the Program

```bash
python src/lab4.py
```

## Project Structure

```
lab_4/ 
│ 
├─ README.md 
├─ requirements.txt 
│ 
├─ src/ 
│   └─ lab4.py
│ 
└─ report/ 
    └─ answers.md 
```

## Description of program

The program prints several structured sections (A–G + Demonstration), each focused on a specific Python concept:

- Higher-Order Function  
  Prints a list where a function passed as an argument is applied to each element.
- Map  
  Prints transformed lists such as squares root and string conversions
- Filter  
  Prints filtered lists such as even numbers and values greater than 10
- Map/Filter vs comprehension  
  Prints two identical results to show both approaches produce the same output
- Simple Decorator  
  Prints increasing call numbers before each function execution
- Decorator with Arguments  
  Prints modified function output with a prefix.
- Caching Decorator   
  Prints recursive calls without caching and then shows optimized execution with caching, highlighting reduced repeated computations

The output is designed to demonstrate how Python can efficiently process data and optimize computations using higher-order functions and decorators.