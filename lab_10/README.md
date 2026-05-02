# Report Tool

## Description

**Report Tool** is a command-line Python utility for processing numeric data.

It allows you to:
- read numbers from a file,
- parse and analyze numeric data,
- generate reports,
- save results in text or JSON format,
- log execution steps for debugging and transparency.

---

## How to Run

Run the tool as a CLI application:

```bash
python -m report_tool --input <file> --out <file> --format text|json --log-level LEVEL
````

---

## CLI Arguments

| Argument      | Description                      | Required | Example         |
| ------------- | -------------------------------- | -------- | --------------- |
| `--input`     | Path to input file with numbers  | Y        | `data.txt`      |
| `--out`       | Path to output file              | Y        | `report.txt`    |
| `--format`    | Output format (`text` or `json`) | N        | `json`          |
| `--log-level` | Logging level                    | N        | `INFO`, `DEBUG` |

---

## Examples

### Text report

```bash
python -m report_tool --input data.txt --out report.txt --format text --log-level INFO
```

### JSON report

```bash
python -m report_tool --input data.txt --out report.json --format json --log-level WARNING
```

---

## Input Format

The tool supports flexible number separators:

```
1, 2; 3 4.5
```

Supported separators:

* comma `,`
* semicolon `;`
* whitespace

---

## Output Formats

### 1. Text (human-readable)

```
Number Report
count: 4
sum: 10.5
min: 1
max: 4.5
mean: 2.63
sorted: [1.0, 2.0, 3.0, 4.5]
```

---

### 2. JSON (machine-readable)

```json
{
    "count": 4,
    "sum": 10.5,
    "min": 1,
    "max": 4.5,
    "mean": 2.625
}
```

---

## Project Structure

```
lab10/
  README.md
  requirements.txt

  src/
    report_tool/
      __init__.py
      __main__.py
      numbers.py
      report.py
      storage.py

  report/
    report.md
```

---

## Requirements

* Python 3.10+
* No external dependencies

---
