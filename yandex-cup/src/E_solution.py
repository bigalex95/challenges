# ============================================================================
# The Legend of Icarus (Легенда об Икаре)
# ============================================================================


def solve():
    import sys

    # Binary search for N (interactive)
    left = 1
    right = 10**18

    while left < right:
        mid = (left + right) // 2
        print(mid, flush=True)

        response = input().strip()

        if response == "wet":
            left = mid + 1
        elif response == "ok":
            right = mid
        else:  # "fail"
            sys.exit(0)

    print(f"! {left}", flush=True)
