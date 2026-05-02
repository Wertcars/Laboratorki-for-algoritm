from typing import List, Dict
import re


def parse_numbers(text: str) -> List[float]:
    """
    Parse a string into a list of floats.
    Supports ',', ';' and whitespace as separators.
    """
    pieces = re.split(r"[,\s;]+", text.strip())

    numbers = []
    for p in pieces:
        if p:
            try:
                numbers.append(float(p))
            except ValueError:
                raise ValueError(f"Invalid number: {p}")

    return numbers


def analyze_numbers(numbers: List[float]) -> Dict[str, float]:
    """
    Analyze a list of numbers and return statistics.
    """
    if not numbers:
        raise ValueError("Numbers must not be empty")

    total = sum(numbers)
    count = len(numbers)

    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": total / count,
    }


if __name__ == "__main__":
    print("Module: numbers.py")
    print("Purpose: Parse text into numbers and perform basic analysis.")
    print()

    print("Public functions:")
    print(" - parse_numbers(text)")
    print(" - analyze_numbers(numbers)")
    print()
    
    print("Example usage:")

    text = "10, 5, 20, 15"
    print("Input text:", text)

    numbers = parse_numbers(text)
    print("Parsed numbers:", numbers)

    print("Sorted numbers:", sorted(numbers))

    stats = analyze_numbers(numbers)
    print("Statistics:", stats)