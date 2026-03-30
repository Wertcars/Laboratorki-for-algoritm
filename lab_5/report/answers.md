### 1. What is the purpose of type hints in Python?

Type hints are used to specify the expected types of variables, function arguments, and return values.  
They improve code readability, help developers understand how functions should be used, and allow static type checkers (like mypy) to detect errors before runtime.

---

### 2. What is the difference between Any and a generic type T?

- `Any` means that a variable can be of any type, and no type checking is enforced.  
- A generic type `T` represents a specific type that is unknown but must stay consistent.

Example:  
If a function uses `T`, all values must be of the same type.  
If it uses `Any`, different types can be mixed without warnings.

---

### 3. What does Callable[[int], int] describe?

It describes a function type that:
- takes one argument of type `int`
- returns a value of type `int`

It is commonly used when a function accepts another function as an argument.  
In this case, it specifies what kind of function can be passed (its parameters and return type).

Example:
A function like `apply(func, x)` expects `func` to match this signature, meaning it must accept an `int` and return an `int`.

---

### 4. Why does mypy --strict require more annotations?

`mypy --strict` enforces stricter type checking rules.  
It requires more annotations to avoid ambiguous types and ensure full type safety.

This helps:
- detect more potential errors  
- prevent unintended behavior  
- make the code more reliable and predictable  