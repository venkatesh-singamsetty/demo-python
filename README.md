# demo-python

A small example Python project demonstrating package structure, testing, and multiple ways to run the application.
- **Main package**: `myapp` with a `greet(name)` function
- **CLI application**: Command-line interface that accepts a `--name` argument
- **Default behavior**: Prints "Hello, World!" or "Hello, {name}!" if name is provided
- **Tests**: Unit tests verify that `greet()` works correctly using pytest
- **Multiple run methods**: Can be run via `python run.py`, `python -m myapp.main`, or installed console script `demo-python`

## Project Structure

```
demo-python/
├── setup.py          # Package setup configuration
├── requirements.txt  # Dependencies (pytest)
├── run.py           # Demo runner script
├── src/
│   └── myapp/       # Main package
│       ├── __init__.py
│       └── main.py  # CLI with greet() function
└── tests/
    └── test_main.py # Unit tests
```

## Prerequisites

- **Python 3.8 or higher**

Tested with:
- Python: `3.13.11`


Install dependencies (recommended in a virtual environment):
```bash
cd /Users/venkat/workspace/gitRepos/demo-python
python3 -m venv .venv
source .venv/bin/activate
# Install package in editable mode
pip install -e .
```

Run tests:
```bash
pytest -q
```

Run the app:
```bash
python run.py --name Venkat
# or
python -m myapp.main --name Venkat
# or use the installed console script
demo-python --name Venkat
```

## If we don't have setup.py, we can use the following commands:
Run tests:
```bash
PYTHONPATH=src pytest -q
```

Run the app:
```bash
PYTHONPATH=src python run.py --name Venkat
# or
PYTHONPATH=src python -m myapp.main --name Venkat
```
