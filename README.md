# Countdown Timer

Simple command\-line countdown timer written in Python. Prompts for a number of seconds and prints the remaining time in HH:MM:SS format until it reaches zero.

## Requirements

- Python 3.8+

## Install (Windows / PowerShell)

Create and activate a virtual environment, then run:
    python -m venv .venv
    .\.venv\Scripts\Activate
    pip install --upgrade pip

## Run

From the project folder:
    python `coundown%20timer.py`

## Usage

- Enter the time in seconds when prompted.
- The script prints remaining time each second until `00:00:00` and then prints `Times UP!`.

## Quick fixes & suggestions

- Filename: consider renaming `coundown%20timer.py` to `countdown_timer.py` (no spaces or percent encoding).
- Input validation: ensure the script converts input to an integer and handles non\-numeric or negative input.
- Interrupts: handle `KeyboardInterrupt` to exit cleanly.
- Accuracy: for long timers, consider using `time.monotonic()` to avoid drift instead of repeated `time.sleep(1)`.

## Troubleshooting

- If nothing appears, confirm you run the script with the correct Python interpreter and that `python` is in PATH.
- If input causes a crash, provide only integers (or improve the script to validate input).

## Contributing

Open issues or PRs. Keep changes small and test on Windows.
