def convert(A):
    x = [int(s) for s in A.splitlines()]

    return x

def jumps(A):
    index = 0
    count = 0

    while index < len(A):
        current = A[index]
        A[index] += 1
        index += current
        count += 1

    return count

def hops(A):
    index = 0
    count = 0

    while index < len(A):
        current = A[index]
        if current >= 3:
            A[index] -= 1
        else:
            A[index] += 1
        index += current
        count += 1

    return count
