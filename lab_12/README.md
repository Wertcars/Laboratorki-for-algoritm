# Async Tool

## Description

**Async Tool** is a Python CLI utility for processing batches of asynchronous tasks with different execution strategies.

It supports:

* sequential execution,
* fully concurrent execution,
* limited concurrency execution.

Key features:

* async task processing with `asyncio`,
* configurable error handling,
* structured JSON input/output,
* execution logging,
* concurrency control via semaphores.

The project also includes a full test suite covering both unit and CLI behavior.

---

## Run

```bash
python -m async_tool input.json [OPTIONS]
```

---

## CLI Options

| Option                | Description                                         |
| --------------------- | --------------------------------------------------- |
| `input.json`          | Path to JSON file with tasks                        |
| `--mode`              | Execution mode: `sync`, `async`, `limited`          |
| `--limit`             | Concurrency limit (for `limited` mode)              |
| `--continue-on-error` | Continue execution after failures                   |
| `--log-level`         | Logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |

---

## Execution Modes

### Sequential (`sync`)

Tasks execute one by one.

```bash
python -m async_tool tasks.json --mode sync
```

### Concurrent (`async`)

All tasks run concurrently.

```bash
python -m async_tool tasks.json --mode async
```

### Limited concurrency (`limited`)

Concurrency is restricted using a semaphore.

```bash
python -m async_tool tasks.json --mode limited --limit 2
```

---

## Error Handling

### Stop on first error (default)

Execution stops when a task fails.

### Continue on error

All tasks are processed regardless of failures:

```bash
python -m async_tool tasks.json --continue-on-error
```

---

## Input Format

```json
[
  {"id": 1, "delay": 1, "good": true},
  {"id": 2, "delay": 2, "good": false},
  {"id": 3, "delay": 1, "good": true}
]
```

### Fields

* `id` — task identifier
* `delay` — execution delay in seconds
* `good` — success/failure flag

---

## Output Format

```json
[
  {"id": 1, "status": "done"},
  {"id": 2, "status": "error", "message": "Task failed"},
  {"id": 3, "status": "done"}
]
```

---

## Testing

The project includes automated tests for both core logic and CLI behavior.

### Run tests

```bash
python -m pytest
python -m pytest tests/test_process_item.py -v
python -m pytest tests/test_cli.py -v
```

### Test coverage

#### Unit tests

* `process_item()` behavior
* success/failure handling
* result structure validation

#### CLI tests

* full application execution via subprocess
* async and sync modes
* error handling (`--continue-on-error`)
* output correctness and ordering

CLI tests use:

* `subprocess.run`
* temporary files (`tmp_path`)
* captured stdout/stderr

---

## Project Structure

```text
async_tool/
├── report/
│   └── answers.md
├── src/
│   ├── __init__.py
│   └── async_tool/
│       ├── __main__.py
│       ├── models.py
│       └── processor.py
├── tests/
│   ├── test_process_item.py
│   └── test_cli.py
├── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.11+
* pytest
* mypy

---

## Type Checking

```bash
mypy src --strict
```