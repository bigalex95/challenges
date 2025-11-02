# ============================================================================
# Hills, Greeks, Gags (Горки, греки, гэги)
# ============================================================================


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))

        if n < 3:
            print(0)
            continue

        # Precompute strictly increasing lengths ending at i (choices to the left)
        left_len = [0] * n
        for i in range(1, n):
            if h[i - 1] < h[i]:
                left_len[i] = left_len[i - 1] + 1
            else:
                left_len[i] = 0

        # Precompute strictly decreasing lengths starting at i (choices to the right)
        right_len = [0] * n
        for i in range(n - 2, -1, -1):
            if h[i] > h[i + 1]:
                right_len[i] = right_len[i + 1] + 1
            else:
                right_len[i] = 0

        # Sum contributions for each peak m
        total = 0
        for m in range(1, n - 1):
            if left_len[m] > 0 and right_len[m] > 0:
                total += left_len[m] * right_len[m]

        print(total)
