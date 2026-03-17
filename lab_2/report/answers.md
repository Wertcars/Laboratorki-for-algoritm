## Task A - Truthiness

Python treats empty containers (like `[]`, `{}`, `""`) as `False` because they represent the absence of elements (i.e. “nothing”).  
This follows Python’s design principle where objects that are “empty” or “zero-like” evaluate to `False`, making conditions more intuitive and readable.

## Task B - Identity vs Equality

`is` should be used when you want to check if two variables refer to the ***same object in memory*** (identity), not just if they have equal values.

Typical use cases:
- comparing with `None` (`x is None`)
- checking if two variables point to the exact same object

`==` should be used when comparing ***values***.

## Task D - Pattern Matching

`match` is convenient for analysing structured data because it allows you to:
- directly match the ***shape and structure*** of data (like tuples)
- extract values
- write clearer and more readable code compared to multiple `if/elif`

It reduces boilerplate and makes logic easier to understand.

## Task F - Generators

1. Difference between list comprehension and generator expression

    - List comprehension (`[x for x in ...]`) creates theentire list in memory immediately
    - Generator expression (`(x for x in ...)`) produces values one at a time on demand

    Generators are more memory-efficient.

2. Why are generators considered lazy?

    Generators are called ***"lazy"*** because they do not compute all values at once. They generate each value only when it is needed (during iteration).

3. What happens when a generator finishes execution?

    When a generator finishes:
    - it raises a `StopIteration` exception internally
    - iteration stops automatically (e.g. in a `for` loop)