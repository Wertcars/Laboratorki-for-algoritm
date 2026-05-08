## 1. Why does await inside a loop lead to sequential execution?

Because each iteration waits for the current coroutine to finish before starting the next one.

---

## 2. How does asyncio.gather change behavior?

`asyncio.gather` runs multiple coroutines concurrently and waits for all of them together.

---

## 3. What happens if one task fails in async mode without --continue-on-error?

The exception propagates, remaining execution stops, and the program exits with a non-zero status code.

---

## 4. Why is semaphore needed?

A semaphore limits the number of simultaneously running coroutines and helps control resource usage.

---

## 5. When should async NOT be used?

Async should not be used for CPU-intensive tasks or programs without asynchronous I/O operations.