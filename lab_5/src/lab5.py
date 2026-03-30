# Task A - Basic Type Hints

print("Task A - Basic Type Hints")
print()

def add(a: int, b: int) -> int:
    return a + b

def square_list(data: list[int]) -> list[int]:
    return [x * x for x in data]

print("Result of add(3, 4):", add(3, 4))
print("Result of square_list([1,2,3,4]):", square_list([1, 2, 3, 4]))

print("-------------------------------------------------")
# Task B - Typed Collections
print("Task B - Typed Collections")
print()

def filter_even(data: list[int]) -> list[int]:
        return [x for x in data if x % 2 == 0]

print("Result of filter_even([1,2,3,4,5,6,7,10]):", filter_even([1, 2, 3, 4, 5, 6, 7, 10]))

print("-------------------------------------------------")
# Task C - Optional
print("Task C - Optional")
print()

def find(data: list[int], x: int) -> int | None: 
        ## -> int | None - also can be written as Optional[int] by using from typing import Optional
        for item in data:
            if item == x:
                return item
        return None

print("Result of find([1,2,3], 2):", find([1, 2, 3], 2))
print("Result of find([1,2,3], 5):", find([1, 2, 3], 5))

print("-------------------------------------------------")
# Task D - Function Type
from collections.abc import Callable

print("Task D - Function Type")
print()

def apply(func: Callable[[int], int], x: int) -> int:
    ## Callable[[int], int] - using to specify that func is a function that takes an int and returns an int
    return func(x)

print("Result of apply(lambda x: x+1, 5):", apply(lambda x: x + 1, 5))
print("Result of apply(lambda x: x*2, 5):", apply(lambda x: x * 2, 5))

print("-------------------------------------------------")
# Task E - Simple Decorator
from typing import TypeVar

print("Task E - Generics")
print()

G = TypeVar('G')
# TypeVar - share a type across multiple function signatures, allowing us to write functions that can operate on any type while still maintaining type safety.

def first(items: list[G]) -> G:
    return items[0]

print("Result of first([1,2,3]):", first([1, 2, 3]))
print("Result of first(['a','b','c']):", first(['a', 'b', 'c']))


print("-------------------------------------------------")
# Task F - Function Returning Function
print("Task F - Function Returning Function")
print()

def make_multiplier(k: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * k
    return multiplier

tryple = make_multiplier(3)
print("tryple(5):", tryple(5))

print("-------------------------------------------------")
# Task G - Caching Decorator
print("Task G - Pipeline")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = sum(x**2 for x in numbers if x % 2 == 0)

print("Pipeline result:", result)