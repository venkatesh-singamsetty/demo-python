# demo-python

This folder now contains a small example Python project.

- `src/myapp` — example package with `greet()` and CLI `main()`.
- `run.py` — demo runner script (call with `python run.py`).
- `tests` — pytest unit tests for the package.
- `requirements.txt` — lists `pytest`.

Prerequisites:
- Python 3.8+

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
