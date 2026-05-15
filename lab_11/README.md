# Async Batch Processor

## Description

**Async Batch Processor** is a command-line Python utility for processing batches of asynchronous tasks.

The tool supports multiple execution strategies:
- sequential execution,
- fully concurrent execution,
- limited concurrency execution.

It also provides:
- configurable error handling,
- JSON input/output,
- execution logging,
- concurrency control with semaphores.

The project demonstrates the difference between synchronous and asynchronous task processing using `asyncio`.

---

## Installing

### 1. Create a virtual environment
It is recommended to create a virtual environment to isolate dependencies:

```
cd lab_11
python -m venv .venv
```
### Activate it:

On Windows:
```
.venv\Scripts\activate
```
On Linux/macOS:
```
source .venv/bin/activate
```

### Install dependencies:

```
pip install -r requirements.txt
```

---

## How to Run

Run the tool as a CLI application:

```bash
python -m async_tool input.json [OPTIONS]
````

---

## CLI Arguments

| Argument              | Description                            | Required | Example                  |
| --------------------- | -------------------------------------- | -------- | ------------------------ |
| `input.json`          | Path to input JSON file                | Y        | `tasks.json`             |
| `--mode`              | Execution mode                         | N        | `sync`, `async`          |
| `--limit`             | Concurrency limit for limited mode     | N        | `--limit 3`              |
| `--continue-on-error` | Continue processing after task failure | N        | `--continue-on-error`    |
| `--log-level`         | Logging level                          | N        | `INFO`, `DEBUG`, `ERROR` |

---

## Execution Modes

### 1. Sequential Mode (`sync`)

Tasks are processed one by one.

```bash
python -m async_tool tasks.json --mode sync
```

---

### 2. Async Mode (`async`)

All tasks run concurrently using `asyncio.gather`.

```bash
python -m async_tool tasks.json --mode async
```

---

### 3. Limited Concurrency Mode (`limited`)

Tasks run concurrently with a concurrency limit using `asyncio.Semaphore`.

```bash
python -m async_tool tasks.json --mode limited --limit 2
```

---

## Error Handling

### Stop on First Error (default)

If a task fails, the program stops immediately and exits with a non-zero code.

```bash
python -m async_tool tasks.json --mode async
```

---

### Continue on Error

All tasks are processed even if some fail.

```bash
python -m async_tool tasks.json --mode async --continue-on-error
```

Failed tasks produce error results:

```json
{
    "id": 2,
    "status": "error",
    "message": "Task 2 failed"
}
```

---

## Logging

Supported logging levels:

* `DEBUG`
* `INFO`
* `WARNING`
* `ERROR`

Example:

```bash
python -m async_tool tasks.json --log-level INFO
```

---

## Input Format

Input file must contain a JSON array of tasks.

Example:

```json
[
    {
        "id": 1,
        "delay": 1,
        "good": true
    },
    {
        "id": 2,
        "delay": 2,
        "good": false
    },
    {
        "id": 3,
        "delay": 1,
        "good": true
    }
]
```

### Task Fields

| Field   | Type    | Description                    |
| ------- | ------- | ------------------------------ |
| `id`    | integer | Unique task identifier         |
| `delay` | float   | Delay in seconds               |
| `good`  | boolean | Whether task succeeds or fails |

---

## Output Format

The program prints JSON results to stdout.

Example:

```json
[
    {
        "id": 1,
        "status": "done"
    },
    {
        "id": 2,
        "status": "error",
        "message": "Task 2 failed"
    },
    {
        "id": 3,
        "status": "done"
    }
]
```

---

## Examples

### Sequential execution

```bash
python -m async_tool tasks.json --mode sync
```

### Concurrent execution

```bash
python -m async_tool tasks.json --mode async
```

### Limited concurrency

```bash
python -m async_tool tasks.json --mode limited --limit 2
```

### Continue processing after failures

```bash
python -m async_tool tasks.json --continue-on-error
```

### Enable INFO logging

```bash
python -m async_tool tasks.json --log-level INFO
```

---

## Project Structure

```text
lab_11/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── async_tool/
│       ├── __init__.py
│       ├── __main__.py
│       ├── models.py
│       └── processor.py
│
└── report/
    └── answers.md
```

---

## Requirements

* Python 3.11+
* `mypy`

---

## Type Checking

Run mypy validation:

```bash
mypy src --strict
```

---

## Notes

* `process_item()` must not be modified.
* Blocking operations (`time.sleep`, `requests`, etc.) must not be used.
* Output order matches input order.
* Each task produces exactly one result.

---

## Expected Outcome

The project clearly demonstrates:

* no performance improvement in sequential mode,
* significant speedup in async mode,
* controlled concurrency with semaphores.
