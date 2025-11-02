# ============================================================================
# Similar Civilizations (Подобные цивилизации)
# ============================================================================


def solve():
    MOD = 10**9 + 7
    n, k = map(int, input().split())

    def mod_pow(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp //= 2
            base = (base * base) % mod
        return result

    def mod_inv(a, mod):
        return mod_pow(a, mod - 2, mod)

    # Precompute C(k, i) for i=0..k and their prefix sums
    comb = [0] * (k + 1)
    comb[0] = 1
    for i in range(1, k + 1):
        # C(k, i) = C(k, i-1) * (k - i + 1) / i
        comb[i] = (comb[i - 1] * (k - i + 1) % MOD * mod_inv(i, MOD)) % MOD

    pref = [0] * (k + 1)
    s = 0
    for i in range(k + 1):
        s = (s + comb[i]) % MOD
        pref[i] = s

    inv_2_k = mod_inv(mod_pow(2, k, MOD), MOD)

    # Expected value E[max] = sum_{v=1..k} P(max >= v)
    result = 0

    for v in range(1, k + 1):
        # P(similarity < v) = sum_{i=0}^{v-1} C(k, i) * (1/2)^k
        # sum_{i=0..v-1} C(k,i) * (1/2)^k
        prob_less_than_v = (pref[v - 1] * inv_2_k) % MOD

        # P(all < v) = (P(similarity < v))^(n-1)
        prob_all_less = mod_pow(prob_less_than_v, n - 1, MOD)

        # P(max >= v) = 1 - P(all < v)
        prob_max_geq_v = (1 - prob_all_less + MOD) % MOD

        result = (result + prob_max_geq_v) % MOD

    print(result)
