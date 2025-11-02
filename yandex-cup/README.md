# Yandex Cup – Solutions and Tests

This repository contains Python solutions for problems A–G and a pytest-based test suite.

## Structure

- `data/` – problem statements (markdown)
- `src/` – solution modules, one per problem: `A_solution.py` … `G_solution.py` (each exposes `solve()`)
- `tests/` – unit tests for solutions; uses input mocking to exercise `solve()`

Note: Filenames use underscores (no hyphens) to be valid Python module names.

## Run tests

```bash
pytest -q
```

## Run a solution manually

```bash
python -m src.A_solution < input.txt
```

Or from Python:

```python
from src.A_solution import solve
solve()  # reads from stdin, writes to stdout
```

## Interactive problems

- Problem E is interactive; the test is marked as skipped. It requires a judge to interact.

## Notes

- Duplicate hyphenated files were removed in favor of canonical underscore modules.
- Basic tests were added for B, C, D, F, and G; A already had comprehensive tests.
