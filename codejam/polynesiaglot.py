def fib(N):
    result = 0
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        result = fib(N - 1) + fib(N - 2)

    return result

def polynesiaglot(C, V, L):
    permutations = 0
    permutations += V ** L
    permutations %= 1000000007
    if L == 1:
        return permutations
    if L % 2 = 0: # L is even
        permutations += (V ** (L / 2)) * (C ** (L / 2))
        permutations %= 1000000007
        if L == 2:
            return permutations
        for exponent in range((L - 1), (L / 2), -1):
            coefficient = blah
            permutations += coefficient * (V ** exponent) * (C ** (L - exponent))
            permutations %= 1000000007
    else: # L is odd
        permutations += (L - 1) * ((V ** (L - 1)) * C)
        permutations %= 1000000007
        if L == 3:
            return permutations
        for exponent in range((L - 1), (L / 2), -1):
            coefficient = blah
            permutations += coefficient * (V ** exponent) * (C ** (L - exponent))
            permutations %= 1000000007

def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        c, v, l = [int(s) for s in raw_input().split(" ")]
        result = polynesiaglot(c, v, l)
        print("Case #{}: {}".format(i, result))

driver()
