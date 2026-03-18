### 1. What does it mean that functions in Python are first-class objects?

It means that functions can be treated like any other object in Python.  
They can be:
- assigned to variables
- passed as arguments to other functions
- returned from functions
- stored in data structures (lists, dictionaries)

Example:
```
def add(x): return x + 10
def mul(x): return x * 10

handlers = {
    "add": add,
    "mul": mul,
}

command = "add"
print(handlers[command](6))
```

Result: ``` 16 ``` 

---

### 2. What is the difference between a function defined with def and a lambda expression?

- `def` creates a named function and can contain multiple statements.
- `lambda` creates an unnamed function and **for python** is limited to a single expression.

Lambdas are typically used for short, simple operations, while `def` is used for more complex logic.

---

### 3. What is a closure?

A closure is a function that remembers variables from its enclosing scope even after that outer function has finished execution.

It allows the inner function to access and modify those captured variables.

---

### 4. In what situations are closures useful?

Closures are useful when:
- you need to preserve state between function calls (e.g. counters)
- you want to create function factories (functions that generate other      functions)
- you want to encapsulate data without using classes
- you need lightweight objects with behavior