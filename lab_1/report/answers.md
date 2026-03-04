## Task A - Binding vs Rebinding

`b` still refers to the old value after `a = 7` because **names in Python are bindings to objects**, not containers that store values.

When we execute:

```python
a = 3
b = a
```

both `a` and `b` are bound to the same integer object `3`.

Later, when we execute:

```python
a = 8
```

this does **not modify the original integer object**. Instead, **rebinding changes the name–object relationship**:  
the name `a` is now bound to a new integer object `7`.

The object `3` itself is not modified (integers are immutable). Since `b` was still bound to the original object `3`, it continues to refer to it.

So:

- names are bindings  
- rebinding changes the name-object relationship  
- objects themselves are not modified  


---

## Task B - Mutation vs Rebinding

Both names see the change because they refer to the **same list object**.

When we write:

```python
a = [1, 2, 3]
b = a
```

both `a` and `b` are bound to the same list in memory.

When we execute:

```python
a.append(5)
```

this is **mutation** - it modifies the existing object in place. Since both names reference the same object, both see the updated content.

### Difference between mutation and rebinding

- **Mutation** changes the internal state of an existing object without changing its identity.  
- **Rebinding** changes which object a name refers to.  

In this case, the list object itself was modified (mutation), so both names reflect the change.


---

## Task C - Function Arguments Are New Bindings

Mutation inside the function affects the caller because **argument passing in Python is binding, not copying**.

When the function is called:

```python
a_append(a)
```

the parameter `lst` becomes a **new local name** bound to the same object as `a`. No copy is created.

So when `lst.append(7)` is executed, it mutates the same list object. Since both `lst` and `a` refer to the same object, the caller sees the change.

However, in:

```python
def a_rebind(lst):
    lst = [7, 7, 8]
```

the assignment creates a new list and rebinds the local name `lst` to it. This rebinding only changes the local name inside the function.

Because:

- parameters are new local names  
- argument passing is binding, not copying  

rebinding inside the function does not affect the caller’s variable.


---

## Task D - Default Argument Trap

The list keeps growing because **default values are evaluated once**, at function definition time — not each time the function is called.

In:

```python
def g(lst=[]):
```

the empty list is created once and stored as the default value.

Each time `g()` is called without an argument, **the same object is reused across calls**.

Since the function mutates the list with `append(9)`, the list grows with every call.

So:

- default values are evaluated once  
- the same object is reused across calls  


---

## Task E - Shallow Copy vs Deep Copy

The difference between shallow copy and deep copy becomes visible with **nested objects**.

Given:

```python
a = [[3, 4]]
b = a.copy()
c = copy.deepcopy(a)
```

### Shallow copy

A shallow copy creates a new outer container, but the **nested objects are still shared**.

So `b` is a new list, but `b[0]` refers to the same inner list as `a[0]`.

When the inner list is modified, both `a` and `b` reflect the change.

### Deep copy

A deep copy creates a new outer container **and recursively copies nested objects**.

So `c[0]` is a completely independent inner list.

Modifying the inner list in `b` does not affect `c`.

In summary:

- shallow copy duplicates only the outer object  
- deep copy duplicates nested objects as well  


---

## Task F - Reference Counting (CPython)

The result for small integers like `5` may look unusual because of **CPython optimization**.

CPython uses an optimization where small integers (typically from `-5` to `256`) are pre-created and reused. These objects may have unusually high reference counts.

Additionally, newer versions of CPython introduce the concept of **immortal objects** — objects that are never deallocated and may report very large reference counts.

This behavior is:

- specific to CPython  
- an implementation detail  
- not guaranteed by the Python language specification  

Other Python implementations may behave differently.

Therefore, reference counts for small integers may appear unexpectedly large due to CPython optimization and immortal object handling.
