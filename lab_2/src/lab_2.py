# Task A — Truthiness
print("Task A - Truthiness\n")

values = [0, 1, [], [1], "", "Hello", None]

for i in values:
    print(f"value: {i} -> {bool(i)}")

print("-------------------------------------------------")
# Task B - Identity vs Equality
print("Task B - Identity vs Equality\n")

a = [4, 3, 2]
b = [4, 3, 2]

print("a = ", a)
print("b = ", b)
print(f"a == b -> {a == b}")
print(f"a is b -> {a is b}")

c = a

print(f"\ncreate c = a\n")
print(f"a == c -> {a == c}")
print(f"a is c -> {a is c}\n")

x = 256
y = 256

print("x = ", x) 
print("y = ", y)
print(f"x == y -> {x == y}")
print(f"x is y -> {x is y}")

print("-------------------------------------------------")
# Task C - Control Flow
print("Task C - Control Flow\n")

def describe_number(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif 0 < x < 10:
        return "small positive"
    else:
        return "large positive"

test_numbers = [-3, 0, 3, 10]
for num in test_numbers:
    print(f"{num} -> {describe_number(num)}")

print("-------------------------------------------------")
# Task D - Pattern Matching
print("Task D - Pattern Matching\n")

events = [
    ("click", 10, 20),
    ("keypress", "A"),
    ("quit",)
]

for event in events:
    match event:
        case ("click", x, y):
            print(f"click at {x} {y}")
        case ("keypress", key):
            print(f"key pressed: {key}")
        case ("quit",):
            print("quit event")

print("-------------------------------------------------")
# Task E - Comprehensions
print("Task E - Comprehensions\n")

squares = [x**2 for x in range(1, 21)]
print("Squares:", squares)

even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print("Even squares:", even_squares)

square_dict = {x: x**2 for x in range(1, 11)}
print("Square dict:", square_dict)

print("-------------------------------------------------")
# Task F - Generators
print("Task F - Generators\n")

def even_numbers(limit):
    for i in range(0, limit):
        if i % 2 == 0:
            yield i

print("Even numbers up to 10:")
for num in even_numbers(10):
    print(num)

print("-------------------------------------------------")
# Additional - Generator Expression
print("Additional - Generator Expression\n")

LIMIT = 1_000_000

result = sum(x**2 for x in range(1_000_000) if x % 2 == 0)
print(f"Sum of squares of even numbers < {LIMIT:_}: {result:_}")