def permute(A):
    # Argument:
    #   A is a list of integers that might contain duplicates
    # Output:
    #   Return a list of all possible unique permutations of the list A
    #   This will be a list of lists
    #   Cannot use library functions for generating permutations

    permutations = []
    hPermutations = set()
    tPermutations = []
    lPermutations = []
    B = []
    if len(A) == 1:
        B = list(A)
        return [B]
    else:
        last = A.pop()
        rPermutations = permute(A)
        for each in rPermutations:
            i = 0
            while i <= len(each):
                pList = each.copy()
                pList.insert(i, last)
                permutations.append(pList)
                i += 1

    for item in permutations:
        tupleItem = tuple(item)
        hPermutations.add(tupleItem)
    tPermutations = list(hPermutations)
    for t in tPermutations:
        listItem = list(t)
        lPermutations.append(listItem)

    return lPermutations


def permuteBasic(A):
    # Not time efficient

    permutations = []
    B = []
    if len(A) == 1:
        B = list(A)
        return [B]
    else:
        last = A.pop()
        rPermutations = permute(A)
        for each in rPermutations:
            i = 0
            while i <= len(each):
                pList = each.copy()
                pList.insert(i, last)
                sPermutations = set()
                for item in permutations:
                    tupleItem = tuple(item)
                    sPermutations.add(tupleItem)
                tuplePlist = tuple(pList)
                if tuplePlist not in sPermutations:
                    permutations.append(pList)
                i += 1
    return permutations


def longestConsecutive(A):
    # Argument:
    #   A is a list of unsorted integers
    # Output:
    #   Return an integer representing the length of the longest consecutive
    #   elements sequence. This should run in O(n) complexity.
    hash = set(A)
    longest = 0

    for ival in A:
        streak = 0
        # Is it the start of a sequence?
        if (ival - 1) not in hash:     # this is a start
            next = ival
            while(next in hash):        # if the next in the sequence is present
                streak += 1             # increment the streak
                next += 1
        longest = max(longest, streak)

    return longest
