# Task A - Functions as Objects
print("Task A - Functions as Objects\n")

def apply_twice(func, x):
    return func(func(x))

print("Result of lambda func:", apply_twice(lambda x: x + 2, 4))
print("Result of abs func:", apply_twice(abs, -12))

def sqrt(x):
    return x ** 0.5

print("Result of sqrt func:", apply_twice(sqrt, 16))

print("-------------------------------------------------")
# Task B - Sorting with Lambda
print("Task B - Sorting with Lambda\n")

people = [
    ("Alice", 25),
    ("Bob", 20),
    ("Carol", 30),
    ("Dave", 22)
]

sorted_by_name = sorted(people, key=lambda x: x[0])
sorted_by_age = sorted(people, key=lambda x: x[1])

print("Sorted by name:")
print(", ".join(f"{name}: {age}" for name, age in sorted_by_name), "\n")

print("Sorted by age:")
print(", ".join(f"{name}: {age}" for name, age in sorted_by_age))

print("-------------------------------------------------")
# Task C - Function Factory
print("Task C - Function Factory\n")

def make_multiplier(k):
    def multiplier(n):
        return n * k
    return multiplier

times4 = make_multiplier(4)
times8 = make_multiplier(8)

print("Result of times4(6):", times4(6))
print("Result of times8(4):", times8(4))

print("-------------------------------------------------")
# Task D - Closure Counter
print("Task D - Closure Counter\n")

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()

print("Result for the first c():", c())
print("Result for the second c():", c())
print("Result for the third c():", c())

print("-------------------------------------------------")
# Task E - Lambda vs def
print("Task E - Lambda vs def\n")

def square(x):
    return x * x

square_lambda = lambda x: x * x

print("Square of 8 by def:", square(8))
print("Square of 8 by lambda:", square_lambda(8))

print("-------------------------------------------------")
# Task F - Functional Composition
print("Task F - Functional Composition\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = sum((lambda x: x ** 2)(n) for n in numbers if n % 2 == 0)

print("Sum of squares of even numbers:", " + ".join(f"{n}**2" for n in numbers if n % 2 == 0), f"= {result}")

print("-------------------------------------------------")