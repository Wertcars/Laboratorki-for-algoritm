from pathlib import Path


def save_report(report_content: str, filename: str) -> str:
    """
    Save report text to a file and return the absolute path.
    """
    path = Path(filename)
    path.write_text(report_content, encoding="utf-8")
    return str(path.absolute())

def read_file(filepath: str) -> str:
    """
    Read file content back into a string.
    """
    path = Path(filepath)
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    print("Module: storage.py")
    print("Purpose: Handles saving and loading reports to/from disk.\n")

    print("Public functions:")
    print(" - save_report(report_content, filename)")
    print(" - read_file(filepath)")
    print()

    print("Example usage:")
    print("  path = save_report('My Report', 'report.txt')")
    print("  content = read_file(path)")