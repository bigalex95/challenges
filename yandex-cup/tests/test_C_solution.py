import builtins
import sys
from io import StringIO

from src.C_solution import solve


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


def test_single_statue_zero_moves():
    # n=1, statue already at (1,1) -> 0 moves
    result = run_with_input("1\n1 1\n")
    assert result.strip() == "0"
