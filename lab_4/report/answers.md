### 1. What is a higher-order function?

A higher-order function is a function that either:
- takes another function as an argument, or
- returns a function as a result.

Example: `map`, `filter`, or user-defined functions like `apply`.

---

### 2. What is the difference between map and list comprehension?

- `map` applies a function to each element of an iterable and returns an iterator.
- List comprehension is a more readable and Pythonic way to create lists with optional conditions.

Example:

```
map:
map(lambda x: x*5, [3,4,6]) → 15, 20, 30 (iterator)

list:
list(map(...)) → [15, 20, 30]
```

List comprehension is usually preferred because it is clearer and more flexible.

---

### 3. What is a decorator?

A decorator is a function that wraps another function to modify or extend its behavior without changing the original function code.

---

### 4. What is the difference between a simple decorator and a decorator with arguments?

- A simple decorator takes only the function as input.
- A decorator with arguments takes additional parameters and returns a decorator.

It usually has an extra nested function layer.

---

### 5. Why is caching useful?

Caching stores previously computed results and reuses them when the same inputs occur again.

It helps:
- avoids repeated computations
- significantly improves performance
- reduces execution time in recursive functions
- prevents unnecessary recalculations
- makes algorithms more efficient (especially for recursion like Tribonacci)