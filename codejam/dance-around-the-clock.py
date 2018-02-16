def swapRight(dancers):
    for index in range(0, len(dancers), 2):
        temp = dancers[index]
        dancers[index] = dancers[index + 1]
        dancers[index + 1] = temp
    return dancers

def swapLeft(dancers, D):
    # swap the 12'o'clock dancer
    temp = dancers[0]
    dancers[0] = dancers[D - 1]
    dancers[D - 1] = temp
    # swap the other dancers
    for index in range(2, D, 2):
            temp = dancers[index]
            dancers[index] = dancers[index - 1]
            dancers[index - 1] = temp

def dance(D, K, N):
    dancers = []
    for d in range(D):
        dancers.append(d + 1)
    for n in range(N % D):
        if n % 2 == 1:
            swapLeft(dancers, D)
        else:
            swapRight(dancers)
    k = dancers.index(K)
    if k == 0:
        dancer_left = dancers[k + 1]
        dancer_right = dancers[D - 1]
    elif k == (D - 1):
        dancer_right = dancers[D - 2]
        dancer_left = dancers[0]
    else:
        dancer_right = dancers[k - 1]
        dancer_left = dancers[k + 1]

    return [dancer_left, dancer_right]

def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        d, k, n = [int(s) for s in raw_input().split(" ")]
        result = dance(d, k, n)
        print("Case #{}: {} {}".format(i, result[0], result[1]))

driver()
