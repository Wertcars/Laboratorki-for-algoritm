# Task A - Higher-Order Function
from operator import call

print("Task A - Higher-Order Function")
print()

def apply(func, data):
    result = []
    for x in data:
        # applies the function func to each element x in data and appends the result to the result list
        result.append(func(x))
    return result

print("Result of applying square root:", apply(lambda x: x ** 0.5, [64, 16, 4]))

print("-------------------------------------------------")
# Task B - Map
print("Task B - Map")
print()

example_list = [11, 22, 33, 44]

squares = list(map(lambda x: x ** 2, example_list)) ## squares elements of example_list
strings = list(map(lambda x: str(x), example_list)) ## converts elements of example_list to strings

print("Squares for", example_list, ":", squares)
print("Conversion of example_list to strings:", example_list, ":", strings)

print("-------------------------------------------------")
# Task C - Filter
print("Task C - Filter")
print()

example_list = [-6, 2, 7, 14, 27, 28, 36, 94, 101]

evens = list(filter(lambda x: x % 2 == 0, example_list)) ## filters even numbers from the example_list
greater_than_10 = list(filter(lambda x: x > 10, example_list)) ## filters numbers greater than 10 from the example_list

print("Evens from example_list:", evens)
print("Values from example_list which are greater than 10:", greater_than_10)

print("-------------------------------------------------")
# Task D - Map/Filter vs comprehension
print("Task D - Map/Filter vs comprehension")
print()

example_list = [4, 8, 12, 13, 15, 18, 22, 23]

result_map_filter = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, example_list))) ## filters even numbers from example_list and then squares them using map
result_comp = [x**2 for x in example_list if x % 2 == 0] ## filters even numbers from example_list and then squares them using list comprehension

print("Map+Filter:", result_map_filter)
print("Comprehension:", result_comp)

print("-------------------------------------------------")
# Task E - Simple Decorator
print("Task E - Simple Decorator")
print()

def call_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"call #{count}") # adds a call count before calling the function
        return func(*args, **kwargs)
    
    return wrapper

@call_counter
def greet():
    print("Hello!")

greet()
greet()
greet()
greet()
print("call #5")
print("HELLO!!! hear me pls :(")

print("-------------------------------------------------")
# Task F - Decorator with arguments
print("Task F - Decorator with arguments")
print()

def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{text}: {result}" #adds the prefix to the result of the function
        return wrapper
    return decorator


@prefix("INFO") ## creates a decorator with the prefix "INFO"
def get_data():
    return "data"

print(get_data())

print("-------------------------------------------------")
# Task G - Caching Decorator
print("Task G - Caching Decorator with tribonacci")
print()

def cache(func):
    cache_data = {}

    def wrapper(n):
        ## cache n if it is already computed
        if n in cache_data:
            print(f"[cache hit] tribonacci({n}) = {cache_data[n]}")
            return cache_data[n]

        ## compute n if it is not in cache
        print(f"[compute] tribonacci({n})")
        result = func(n)
        cache_data[n] = result
        return result

    return wrapper

def tribonacci(n):
    # func to compute the nth tribonacci number without caching
    print(f"compute tribonacci({n})")
    if n <= 2:
        return n
    return (tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3))

print("Result for tribonacci(5):", tribonacci(5))
print()

print("Tribonacci with cache decorator")
print()

@cache
def tribonacci(n):
    # func to compute the nth tribonacci number with caching
    if n <= 2:
        return n
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

print("Result for tribonacci(5):", tribonacci(5))