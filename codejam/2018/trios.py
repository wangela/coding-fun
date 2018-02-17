def play_trios(n):
    result = 0.0
    return result

def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        N = int(raw_input())
        result = play_trios(N)
        print("Case #{}: {}".format(i, result))

driver()
