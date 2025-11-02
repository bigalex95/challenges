# ============================================================================
# Two out of Three (Два из трёх)
# ============================================================================


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def solve():
    a, b, c = map(int, input().split())
    n = int(input())

    MAX_VAL = 10**18

    ab = lcm(a, b)
    ac = lcm(a, c)
    bc = lcm(b, c)
    abc = lcm(ab, c)

    def count_up_to(x):
        count_ab = x // ab - x // abc
        count_ac = x // ac - x // abc
        count_bc = x // bc - x // abc
        return count_ab + count_ac + count_bc

    left, right = 1, MAX_VAL
    result = -1
    while left <= right:
        mid = (left + right) // 2
        cnt = count_up_to(mid)
        if cnt >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    if result == -1 or result > MAX_VAL:
        print(-1)
    else:
        if count_up_to(result) == n:
            while result >= 1 and count_up_to(result) == count_up_to(result - 1):
                result -= 1
            div_a = result % a == 0
            div_b = result % b == 0
            div_c = result % c == 0
            if (div_a + div_b + div_c) == 2:
                print(result)
            else:
                print(-1)
        else:
            print(-1)
