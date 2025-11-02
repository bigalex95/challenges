import builtins
import sys
from io import StringIO

from src.G_solution import solve


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


def test_single_node_tree():
    # n=1, q=1, single word 'a', query at node 1 with string 'a' -> 1
    data = "\n".join(
        [
            "1 1",  # n q
            "a",  # word for node 1
            # no edges (n-1)
            "1 a",  # query: v=1, t='a'
            "",
        ]
    )
    result = run_with_input(data)
    assert result.strip() == "1"
