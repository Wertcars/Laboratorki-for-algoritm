## 1. What was added

In this lab, the existing `report_tool` package was extended with several new capabilities:

### CLI interface
A command-line interface was implemented using `argparse`.  
The tool now supports arguments such as:
- `--input` - input file path
- `--out` - output file path
- `--format`- output format (text or json)
- `--log-level` - logging level

This allows the tool to be used directly from the terminal without modifying the code.

---

### File input/output
The tool now reads numeric data from an external file instead of using hardcoded values.  
The result is written to a user-specified output file.

This makes the tool usable in real workflows and scripts.

---

### JSON output
In addition to the human-readable text report, the tool now supports JSON output.

JSON output:
- is generated directly from analysis results,
- provides structured data,
- can be used by other programs or services.

---

### Logging
Logging was added using the `logging` module.

The tool logs the main steps:
- reading input file
- parsing numbers
- analyzing data
- generating report
- saving output

Logging level is controlled via `--log-level`, allowing flexible verbosity.

---

## 2. How the tool changed

Previously (Lab 09), the tool:
- worked as a demo-style script,
- used hardcoded input,
- required manual execution in Python,
- printed results directly.

Now (Lab 10), the tool:
- works as a CLI application,
- accepts external input via files,
- produces output files,
- supports multiple output formats,
- provides structured logging.

The tool evolved from a simple demo into a usable command-line utility.

---

## 3. Why these changes matter

### CLI improves usability and automation
A command-line interface allows:
- easy execution from terminal,
- integration with scripts,
- automation of repetitive tasks.

---

### JSON is useful for machine-readable output
JSON format:
- is structured and standardized,
- can be easily parsed by other programs,
- enables integration with APIs and data pipelines.

---

### Logging improves debugging and transparency
Logging:
- shows what the tool is doing step by step,
- helps identify errors,
- allows controlling output verbosity.

This makes the tool more reliable and easier to debug.