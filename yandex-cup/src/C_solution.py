# ============================================================================
# Easter Island Statues (Статуи острова Пасхи)
# ============================================================================


def solve():
    n = int(input())
    statues = []

    for _ in range(n):
        r, c = map(int, input().split())
        statues.append((r - 1, c - 1))  # 0-indexed

    # We need to assign each statue to a unique row and unique column
    # This is a bipartite matching problem with minimum cost
    # Use Hungarian algorithm or greedy approach with Manhattan distance

    # For simplicity and constraints unknown, use brute force for small n and a heuristic otherwise

    def min_cost_matching():
        INF = float("inf")

        from itertools import permutations

        if n <= 8:  # Small enough for brute force
            min_moves = INF
            for row_perm in permutations(range(n)):
                for col_perm in permutations(range(n)):
                    moves = 0
                    for i in range(n):
                        r, c = statues[i]
                        target_r, target_c = row_perm[i], col_perm[i]
                        moves += abs(r - target_r) + abs(c - target_c)
                    if moves < min_moves:
                        min_moves = moves
            return 0 if min_moves is INF else min_moves
        else:
            # Greedy heuristic: sort by row and column independently
            sorted_by_row = sorted(
                range(n), key=lambda i: (statues[i][0], statues[i][1])
            )
            sorted_by_col = sorted(
                range(n), key=lambda i: (statues[i][1], statues[i][0])
            )

            moves = 0
            for i, idx in enumerate(sorted_by_row):
                moves += abs(statues[idx][0] - i)
            for i, idx in enumerate(sorted_by_col):
                moves += abs(statues[idx][1] - i)

            return moves

    print(min_cost_matching())
