import argparse
import logging

from report_tool import (
    parse_numbers,
    analyze_numbers,
    build_report,
    build_sorted_report,
    save_report,
    read_file,
)
from report_tool.report import build_json_report


def setup_logging(level: str):
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(levelname)s: %(message)s"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Report Tool CLI")

    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--out", required=True, help="Output file path")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level"
    )

    args = parser.parse_args()

    setup_logging(args.log_level)

    logging.info("Reading input file...")
    text = read_file(args.input)

    logging.info("Parsing numbers...")
    numbers = parse_numbers(text)

    logging.info("Analyzing numbers...")
    stats = analyze_numbers(numbers)

    logging.info("Building report...")
    if args.format == "text":
        report = build_sorted_report(numbers, stats)
    else:
        report = build_json_report(stats)

    logging.info("Saving report...")
    output_path = save_report(report, args.out)

    logging.info(f"Done. Report saved to: {output_path}")


if __name__ == "__main__":
    main()