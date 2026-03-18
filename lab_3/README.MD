# Description of lab

This lab demonstrates Python functions as first-class objects, including passing functions as arguments, lambda expressions, closures, and functional composition.

The program consists of six independent tasks (A–F). Each task explores a specific concept using clear examples and printed output.

## Requirement

- Python 3.10+
- Windows/Linux/macOS

## Command to Run the Program

```bash
python src/lab3.py
```

## Project Structure

```
lab03/ 
│ 
├─ README.md 
├─ requirements.txt 
│ 
├─ src/ 
│   └─ lab3.py
│ 
└─ report/ 
    └─ answers.md 
```

## Description of program

The program prints several structured sections (A–F), each focused on a specific Python concept:

- Functions as Objects  
  Prints results of applying different functions twice, e.g. ```apply_twice(lambda x: x+1, 3) → 5```

- Sorting with Lambda  
  Prints sorted lists of people by age and by name

- Function Factory  
  Prints results of generated multiplier functions, e.g. ```times4(6) → 24, times8(4) → 32```

- Closure Counter  
  Prints increasing values from a ```counter()```: 1, 2, 3, showing stored state

- Lambda vs def  
  Prints results of two equivalent implementations to show identical behavior

- Functional Composition    
  Prints the sum of squared even numbers from a list

The output is designed to demonstrate how Python handles functions as objects, closures, and functional-style data processing.