# Description of lab

This lab demonstrates Python expressions and control flow, including truthiness, identity vs equality, conditional statements, pattern matching, comprehensions, and generators.

The program consists of six independent tasks (A-F) and an additional task. Each task explores a specific concept using clear examples and printed output.

## Requirement

- Python 3.10+
- Windows/Linux/macOS

## Project Structure

```
lab02/ 
│ 
├─ README.md 
├─ requirements.txt 
│ 
├─ src/ 
│   └─ your_code 
│ 
└─ report/ 
    └─ answers.md 
```

## Command to Run the Program

```bash
python src/lab_2.py
```

## Description of program

The program prints several structured sections (A–F + Additional), each focused on a specific Python concept:

- Truthiness of different objects  
  (prints values and their boolean evaluation, e.g. `value: [] -> False`)

- Identity vs Equality (`is` vs `==`)  
  (prints comparison results for different cases: equal objects, identical objects, immutable values)

- Control Flow using `if / elif`  
  (prints classification of numbers: negative, zero, small positive, large positive)

- Pattern Matching using `match`  
  (prints processed events such as clicks, keypresses, and quit events)

- Comprehensions (list and dictionary)  
  (prints generated lists and dictionary: squares, even squares, mapping `{x: x²}`)

- Generators and lazy evaluation  
  (prints sequence of even numbers produced by a generator)

- Generator expression (Additional task)  
  (prints the computed sum of squares of even numbers below 1_000_000)

Each section demonstrates:

- Program output for different cases  
- Behavior of Python constructs in practice  
- Clear examples illustrating core concepts  

The output is designed to demonstrate how Python evaluates conditions, processes structured data, and efficiently works with collections and generators.