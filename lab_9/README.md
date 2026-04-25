# Report Tool

## Description

**Report Tool** is a simple Python package for working with numeric data.

It allows you to:

* parse numbers from text input,
* analyze numeric data,
* generate formatted reports,
* save reports to files.

---

## How to Run

Run the tool as a package:

```bash
python -m report_tool
```

---

## How to Use

Example usage in code:

```python
from report_tool import (
    parse_numbers,
    analyze_numbers,
    build_sorted_report,
)

text = "1, 2, 3, 4.5"

numbers = parse_numbers(text)
stats = analyze_numbers(numbers)

report = build_sorted_report(numbers, stats)

print(report)
```

---

## Project Structure

```
lab_9/
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
