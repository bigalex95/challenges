import pytest
from io import StringIO
import sys
import builtins

from src.A_solution import solve


def run_with_input(input_str):
    old_stdin = sys.stdin
    sys.stdin = StringIO(input_str)
    old_print = builtins.print
    output = []

    def mock_print(*args, **kwargs):
        output.append(" ".join(str(a) for a in args))

    builtins.print = mock_print
    try:
        solve()
    finally:
        sys.stdin = old_stdin
        builtins.print = old_print
    return "\n".join(output)


def test_example_1():
    result = run_with_input("2 3 5\n10\n")
    assert result.strip() == "42"


def test_example_2():
    result = run_with_input("5 6 7\n1000000\n")
    assert result.strip() == "13999986"


def test_first_element():
    result = run_with_input("2 3 5\n1\n")
    assert result.strip() == "6"


def test_large_n():
    result = run_with_input("2 3 5\n1000000000000000000\n")
    assert result.strip() == "-1"


def test_all_same():
    result = run_with_input("1 1 1\n1\n")
    assert result.strip() == "-1"
