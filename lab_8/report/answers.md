### 1. How does a for loop work with custom objects?

A `for` loop works with custom objects by calling the `__iter__()` method on the object. This method must return an iterator. Then the loop repeatedly calls `__next__()` on that iterator until a `StopIteration` exception is raised.

---

### 2. What methods are required for iteration?

To support iteration, the following methods are required:

* `__iter__()` — returns an iterator object
* `__next__()` — returns the next element and raises `StopIteration` when the iteration is finished

---

### 3. How does the with statement work internally?

The `with` statement calls the `__enter__()` method at the beginning of the block and the `__exit__()` method at the end.
The `__enter__()` method returns the object that will be used inside the block, while `__exit__()` is responsible for cleanup and receives information about any exception that occurred.

---

### 4. When is **exit** called?

The `__exit__()` method is always called after the execution of the `with` block, regardless of whether an exception occurred or not.
It is used to release resources and perform cleanup operations.

---

### 5. What problem do descriptors solve?

Descriptors solve the problem of uncontrolled attribute access.
They allow defining custom logic for getting and setting attributes, such as validation, type checking, or computed values.

---

### 6. What happens if a descriptor is not used?

If a descriptor is not used, attributes are accessed directly without any validation or control.
This can lead to incorrect or invalid data being assigned (for example, a grade outside the allowed range).

---

### 7. Why is direct iteration preferred over index-based loops in Python?

Direct iteration is preferred because it is more readable and concise.
It eliminates the need to manually manage indices and works with any iterable object.
It also reduces the risk of errors such as accessing elements outside the valid range.

---

### Possible limitations and failure cases

* If `StopIteration` is not raised, the loop may become infinite.
* If `__exit__()` is missing, the `with` statement will not work correctly and may raise an error.
* If validation (descriptor) is not implemented, invalid data can be assigned without any restrictions.
