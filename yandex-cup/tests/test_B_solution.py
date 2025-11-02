import builtins
import sys
from io import StringIO

from src.B_solution import solve


def run_with_input(input_str: str) -> str:
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


def test_single_case_too_short():
    # n < 3 => 0
    result = run_with_input("1\n2\n5 6\n")
    assert result.strip() == "0"


def test_simple_hill_1():
    # [1,2,1] has exactly one hill
    result = run_with_input("1\n3\n1 2 1\n")
    assert result.strip() == "1"


def test_simple_hill_2():
    # [1,3,2,1] has two valid hills with peak at 3: [1,3,2] and [1,3,2,1]
    result = run_with_input("1\n4\n1 3 2 1\n")
    assert result.strip() == "2"
