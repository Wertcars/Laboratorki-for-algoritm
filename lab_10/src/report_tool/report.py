from typing import Any
import json


def build_report(stats: dict[str, Any]) -> str:
    """
    Build a human-readable text report.
    """
    lines = [
        "Number Report",
        f"count: {stats['count']}",
        f"sum: {stats['sum']}",
        f"min: {stats['min']}",
        f"max: {stats['max']}",
        f"mean: {round(stats['mean'], 2)}",
    ]
    return "\n".join(lines)


def build_sorted_report(numbers: list[float], stats: dict[str, Any]) -> str:
    """
    Build a report including sorted numbers.
    """
    base_report = build_report(stats)
    ordered = sorted(numbers)

    return f"{base_report}\nsorted: {ordered}"


def build_json_report(stats: dict[str, Any]) -> str:
    """
    Build JSON formatted report.
    """
    return json.dumps(stats, indent=4)


if __name__ == "__main__":
    print("Module: report.py")
    print("Purpose: Generate formatted text reports from numeric statistics.")
    print()

    print("Public functions:")
    print(" - build_report(stats)")
    print(" - build_sorted_report(numbers, stats)")
    print()

    print("Example usage:")

    example_numbers = [3.4, 1.1, 2.5]
    example_stats = {
        "count": 3,
        "sum": 6,
        "min": 1,
        "max": 3,
        "mean": 2.0,
    }

    print("Basic report:")
    print()
    print(build_report(example_stats))
    print()
    print("Report with sorting:")
    print()
    print(build_sorted_report(example_numbers, example_stats))