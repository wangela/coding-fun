def numRangeWithPrint(A, B, C):
    # Arguments:
    #   A is an array of non-negative integers
    #   B is an integer equal to the minimum of a range
    #   C is an integer equal to the maximum of a range
    # Output:
    #   The number of continuous sub-sequences in the array with sum S in the range [B, C]
    #   B <= S <= C
    #   Continuous sub-sequence means A[i]...A[j] where 0 <= i <= j < size(A)

    sumCount = 0
    currSum = A[0]
    start = 0

    for (i = 1, i < A.size(), i += 1):
        while (currSum > C && start < i):
            currSum -= A[start]
            start += 1
        if currSum >= B:
            sumCount += 1
            continue


    return sumCount

def numRangeBasic(A, B, C):
    # Not the most efficient. O(n^2)

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
