import builtins
import sys
from io import StringIO

from src.F_solution import solve


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


def test_simple_and_mex():
    # All ANDs over [1,1,1] are 1 => MEX is 0
    data = "\n".join(
        [
            "3",
            "1 1 1",
            "1",
            "1 3",
            "",
        ]
    )
    result = run_with_input(data)
    assert result.strip() == "0"
