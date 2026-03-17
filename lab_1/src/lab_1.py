#Task A - Binding vs Rebinding
print("Task A — Binding vs Rebinding")

a = 3
b = a

print(f"\nValua before rebinding a = {a}")
print(f"Valua before rebinding b = {b}")
print(f"ID before rebinding id(a) = {id(a)}")
print(f"ID before rebinding id(b) = {id(b)}")

a = 8
print("\nrebinding a to 8")

print(f"\nValua after rebinding a = {a}")
print(f"Valua after rebinding b = {b}")
print(f"ID before after id(a) = {id(a)}")
print(f"ID before after id(b) = {id(b)}")

print("-------------------------------------------------")

#Task B - Mutation vs Rebinding
print("Task B — Mutation vs Rebinding")

a = [1, 2, 3]  
b = a

print(f"\nValua before append a = {a}")
print(f"Valua before append b = {b}")
print(f"ID before append id(a) = {id(a)}")
print(f"ID before append id(b) = {id(b)}")

a.append(5)
print("\nappending 5 to a")

print(f"\nValua after append a = {a}")
print(f"Valua after append b = {b}")
print(f"ID after append id(a) = {id(a)}")
print(f"ID after append id(b) = {id(b)}")

if id(a) == id(b):
    print(f"\nmemory box still the same id(a):{id(a)} == id(b):{id(b)}")
else:
    print(f"\nmemory box changed id(a):{id(a)} != id(b):{id(b)}")

print("-------------------------------------------------")

#Task C - Function arguments are new bindings
print("Task C — Function arguments are new bindings")

a = []

def a_append(lst):
    lst.append(7)

def a_rebind(lst):
    lst = [7, 7, 8]

print(f"\nValua before append a = {a}")

a_append(a)
print("\nappending 7 to a using function a_append")
print(f"\nValua after append a = {a}")

a_rebind(a)
print("\nrebinding a to [7, 7, 8] using function a_rebind")
print(f"\nValua after rebind a = {a}")

print("-------------------------------------------------")

#Task D — Default argument trap
print("Task D — Default argument trap")

def g(lst=[]):
    lst.append(9)
    return lst

print(f"\nCalling g() first time: {g()}")
print(f"Calling g() second time: {g()}")

print("-------------------------------------------------")
import copy

#Task E — Copy semantics (shallow vs deep)
print("Task E — Copy semantics (shallow vs deep)")

a = [[3, 4]]
b = a.copy()
c = copy.deepcopy(a)

print(f"\nOriginal list a = {a}")
print(f"Shallow copy b = {b}")
print(f"Deep copy c = {c}")

b[0].append(7)
print("\nappending 7 to b")

print(f"\nOriginal list a after modifying b = {a}")
print(f"Shallow copy b after modifying b = {b}")
print(f"Deep copy c after modifying b = {c}")

print("-------------------------------------------------")
import sys

#Task F — Reference counting / GC (CPython)
print("Task F — Reference counting / GC (CPython)")

a = []
print(f"\na = {a}")
print(f"Initial reference count for a: {sys.getrefcount(a)}")

b = a
print(f"creating b by copying a, b = {b}")
print(f"Initial reference count for b: {sys.getrefcount(b)}")

a = 1
print(f"\nRefcount for 1: {sys.getrefcount(a)}")

b = 9875
print(f"Refcount for 9875: {sys.getrefcount(b)}")

print("-------------------------------------------------")