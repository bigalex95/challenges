# ============================================================================
# Decoding Mayan Code (Расшифровка кода Майя)
# ============================================================================


def solve():
    n, q = map(int, input().split())

    sacred_words = []
    for _ in range(n):
        sacred_words.append(input().strip())

    # Build tree
    from collections import defaultdict

    children = defaultdict(list)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        children[u].append(v)

    # For each query
    for _ in range(q):
        line = input().strip().split()
        v = int(line[0])
        t = line[1]

        # Find all tribes subordinate to v (including v itself)
        subordinates = []

        def dfs(node):
            subordinates.append(node)
            for child in children[node]:
                dfs(child)

        dfs(v)

        # Count occurrences of sacred words
        count = 0
        for tribe_id in subordinates:
            word = sacred_words[tribe_id - 1]  # 1-indexed
            # Count all occurrences of word in t
            for i in range(len(t) - len(word) + 1):
                if t[i : i + len(word)] == word:
                    count += 1

        print(count)
