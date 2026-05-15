import json
import subprocess
import sys
from pathlib import Path


def write_input(
    tmp_path: Path,
    data: list[dict],
) -> Path:
    input_file = tmp_path / "input.json"

    input_file.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    return input_file


def run_cli(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "src.async_tool",
            *args,
        ],
        capture_output=True,
        text=True,
        timeout=10,
    )


def test_basic_execution(tmp_path: Path) -> None:
    input_file = write_input(
        tmp_path,
        [
            {
                "id": 1,
                "delay": 0.01,
                "good": True,
            }
        ],
    )

    result = run_cli([str(input_file)])

    assert result.returncode == 0

    output = json.loads(result.stdout)

    assert isinstance(output, list)
    assert output[0]["status"] == "done"


def test_async_mode(tmp_path: Path) -> None:
    input_file = write_input(
        tmp_path,
        [
            {
                "id": 1,
                "delay": 0.01,
                "good": True,
            }
        ],
    )

    result = run_cli(
        [
            str(input_file),
            "--mode",
            "async",
        ]
    )

    assert result.returncode == 0

    output = json.loads(result.stdout)

    assert output == [
        {
            "id": 1,
            "status": "done",
        }
    ]


def test_error_without_flag(tmp_path: Path) -> None:
    input_file = write_input(
        tmp_path,
        [
            {
                "id": 1,
                "delay": 0.01,
                "good": False,
            }
        ],
    )

    result = run_cli([str(input_file)])

    assert result.returncode != 0


def test_error_with_flag(tmp_path: Path) -> None:
    input_file = write_input(
        tmp_path,
        [
            {
                "id": 1,
                "delay": 0.01,
                "good": False,
            }
        ],
    )

    result = run_cli(
        [
            str(input_file),
            "--continue-on-error",
        ]
    )

    assert result.returncode == 0

    output = json.loads(result.stdout)

    assert output[0]["status"] == "error"
    assert "message" in output[0]


def test_output_structure_and_order(
    tmp_path: Path,
) -> None:
    input_file = write_input(
        tmp_path,
        [
            {
                "id": 1,
                "delay": 0.01,
                "good": True,
            },
            {
                "id": 2,
                "delay": 0.01,
                "good": True,
            },
        ],
    )

    result = run_cli(
        [
            str(input_file),
            "--mode",
            "async",
        ]
    )

    assert result.returncode == 0

    output = json.loads(result.stdout)

    assert len(output) == 2

    assert output[0]["id"] == 1
    assert output[1]["id"] == 2