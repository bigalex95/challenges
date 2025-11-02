# ============================================================================
# Sequence (Последовательность)
# ============================================================================


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    # For each query (l, r), compute MEX of all AND ranges
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1  # 0-indexed

        # Compute all possible AND values for subarrays within [l, r)
        # Use rolling set of ANDs for subarrays ending at each position.
        all_ands = set()
        prev = set()
        for x in a[l:r]:
            curr = {x}
            for v in prev:
                curr.add(x & v)
            # Reduce size by exploiting monotonicity (set naturally dedups)
            prev = curr
            all_ands.update(curr)

        # Find MEX
        mex = 0
        while mex in all_ands:
            mex += 1

        print(mex)
