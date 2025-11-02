import builtins
import sys
from io import StringIO

from src.D_solution import solve


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


def test_expected_zero_when_k_zero():
    # With k=0, similarity always 0 -> expected max = 0
    result = run_with_input("2 0\n")
    assert result.strip() == "0"


def test_n2_k1_half():
    # n=2, k=1 -> Expected value is 1/2 modulo MOD
    MOD = 10**9 + 7
    half = (MOD + 1) // 2  # 500000004
    result = run_with_input("2 1\n")
    assert result.strip() == str(half)
