def numRange(A, B, C):
    # Arguments:
    #   A is an array of non-negative integers
    #   B is an integer equal to the minimum of a range
    #   C is an integer equal to the maximum of a range
    # Output:
    #   The number of continuous sub-sequences in the array with sum S in the range [B, C]
    #   B <= S <= C
    #   Continuous sub-sequence means A[i]...A[j] where 0 <= i <= j < size(A)

    sumCount = 0
    P = []

    for index, item in enumerate(A):
        if index == 0:
            P.append(item)
        else:
            P.append(P[index - 1] + item)

    pSum = 0
    end = 0
    for index, item in enumerate(P):
        newPSum = item
        end = index
        while (end < len(P) and (P[end] - pSum) <= C):
            if (P[end] - pSum) > C:
                pSum = newPSum
                continue
            elif (P[end] - pSum) >= B:
                sumCount += 1
            end += 1
        pSum = item

    return sumCount


def numRangeRefactor2(A, B, C):

    sumCount = 0
    P = []

    for index, item in enumerate(A):
        if index == 0:
            P.append(item)
        else:
            P.append(P[index - 1] + item)

    pSum = 0
    end = 0
    print("P length =", len(P))
    for index, item in enumerate(P):
        newPSum = item
        end = index
        while (end < len(P) and (P[end] - pSum) <= C):
            if (P[end] - pSum) > C:
                print("shouldn't happen. end = ", end, ". P[end] = ", P[end])
                pSum = newPSum
                continue
            elif (P[end] - pSum) >= B:
                print("counted one. end =", end, ". P[end] =", P[end])
                sumCount += 1
            end += 1
        pSum = item
        print("pSum now =", pSum)

    return sumCount


def numRangeRefactor(A, B, C):
    # Not the most space efficient.

    sumCount = 0
    currSum = 0

    for ival in A:
        currSum += ival
        print("currSum = ", currSum)
        if (currSum > C):
            break
        elif (currSum >= B):
            sumCount += 1
            print("sumCount = ", sumCount)

    if len(A) > 1:
        sumCount += numRangeRefactor(A[1:], B, C)

    return sumCount


def numRangeBasic(A, B, C):
    # Not the most time efficient. O(n^2)

    sumCount = 0

    for index, ival in enumerate(A):
        if (ival > C): continue
        if (ival >= B):
            sumCount += 1
        currSum = ival
        for jval in A[(index + 1):]:
            currSum += jval
            if (currSum > C):
                break
            elif (currSum < B):
                continue
            else:
                sumCount += 1

    return sumCount
