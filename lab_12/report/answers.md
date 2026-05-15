## 1. What is the difference between unit tests and behavior tests?

Unit tests verify individual functions in isolation, while behavior tests verify the whole application behavior from the user perspective.

---

## 2. Why is subprocess used for CLI testing?

`subprocess` allows running the CLI application exactly as a real user would run it from the command line.

---

## 3. What happens if one async task fails without error handling?

The exception propagates, execution stops, and the program exits with a non-zero status code.

---

## 4. When should you test internal functions vs full system behavior?

Internal functions should be tested for isolated logic correctness, while full system behavior should be tested for user-visible functionality.

---

## 5. What are the risks of time-based tests?

Time-based tests may become unstable because execution speed can vary across systems and environments.