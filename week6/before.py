# DYNAMIC PROGRAMMING
## Simple Array DP
### Length of Longest Subsequence
def longestSubsequenceLength(A):
    # Parameter: A is a list of integers
    # Output: Length of the longest subsequence that is first increasing then decreasing
    # Example: [1 11 2 10 4 5 2 1] -> [1 2 10 4 2 1] -> 6
    longest_sequence_length = 0
    list_length = len(A)
    B = list(A)
    B.reverse()

    li = [1] * list_length # longest increasing from 0 to index i
    ld = [1] * list_length # longest decreasing from index i to end
    ls = [1] * list_length # longestSubsequenceLength for the list up to this point

    for i in range(1, list_length):
        for j in range(i):
            if (A[i] > A[j]) and (li[i] < li[j] + 1):
                li[i] = li[j] + 1

    for x in range(1, list_length):
        for y in range(x):
            if (B[x] > B[y]) and (ld[x] < ld[y] + 1):
                ld[x] = ld[y] + 1

    for l in range(list_length):
        ls[l] = li[l] + ld[list_length - 1 - l] - 1

    longest_sequence_length = max(ls)
    return longest_sequence_length

## Suffix/Prefix DP
### Best Time to Buy and Sell Stocks I
def maxProfitOne(A):
    # Parameter: A is a tuple of integers, the stock price on each day i
    # Output: Find the maximum profit if you were only able to buy one and sell one share of the stock
    # Example: [1 2] -> 1
    #   [4] -> 0
    profits = []
    minSoFar = sys.maxint
    maxProfit = 0

    for i in range(1, len(A)):
        minSoFar = min(minSoFar, A[i - 1])
        maxProfit = max(A[i] - minSoFar, maxProfit)

    return maxProfit

## Adhoc
### Best Time to Buy Sell Stocks II
def maxProfit(A):
    # Parameter: A is a tuple of integers, the stock price on each day i
    # Perform: Buy and sell as many times but must sell before buying again
    # Output: Find the maximum profit if you were able to buy and sell as many times as you wanted
    # Example: [1 2 3] -> 2
    #  [2 3 5 4 8 3 5 1 4] -> [0 1 3 3 7 7 9 9 12] -> 12
    #  [2, 3, 5, 4, 8, 3, 5, 1, 4, 2, 1, 3] ->
    #  [0, 1, 3, 3, 7]
    #  [0, 1, 3, 3, 7, 7, 9, 9, 12, 12, 12, 14] -> 14
    maxProfits = [0]
    lastStart = 0
    lastLoggedProfit = 0


    for i in range(1, len(A)):
        maxProfits.append(maxProfitOne(A[lastStart:i + 1]) + lastLoggedProfit)
        if maxProfits[i] <= maxProfits[i - 1]:
            lastLoggedProfit = maxProfits[i - 1]
            lastStart = i
    #print(maxProfits)
    return maxProfits[-1]

## Matrix DP
### Min Sum Path in Matrix
def isValid(row, col, m, n):
    if row < 0 or row >= m:
        return False
    if col < 0 or col >= n:
        return False
    return True

def minSumPath(A):
    # Parameters: A is a list of a list of integers representing an m x n matrix
    # Perform: Find a path from top left to bottom right which minimizes the sum of all numbers along the path
    # Output: An integer of the minimum sum
    # Example: [[1, 3, 2], [4, 3, 1], [5, 6, 1]] -> 1-3-2-1-1 -> 8
    # Commentary: Whoa, so inefficient compared to the editorial solution (see below). Just need to compare mSP of up and left nodes.
    rows = len(A)
    if rows == 0:
        return 0
    cols = len(A[0])
    if cols == 0:
        return 0
    if rows == 1 and cols == 1:
        return A[0][0]

    sums = []
    first = (0, 0, A[0][0])
    q = deque([first])
    nq = deque([])
    penultimate = rows + cols - 2
    steps = 1
    level_sums = dict()

    while q:
        nq = deque([])
        level_sums = dict()
        while q:
            current = q.popleft()
            current_row = current[0]
            current_col = current[1]
            current_val = current[2]
            if isValid(current_row + 1, current_col, rows, cols):
                next_value = A[current_row + 1][current_col] + current_val
                next_tuple = (current_row + 1, current_col, next_value)
                if (current_row + 1, current_col) in level_sums:
                    level_sums[(current_row + 1, current_col)].append(next_tuple)
                else:
                    level_sums[(current_row + 1, current_col)] = [next_tuple]
                if steps == penultimate:
                    sums.append(next_value)
            if isValid(current_row, current_col + 1, rows, cols):
                next_value = A[current_row][current_col + 1] + current_val
                next_tuple = (current_row, current_col + 1, next_value)
                if (current_row, current_col + 1) in level_sums:
                    level_sums[(current_row, current_col + 1)].append(next_tuple)
                else:
                    level_sums[(current_row, current_col + 1)] = [next_tuple]
                if steps == penultimate:
                    sums.append(next_value)
        for coordinates in level_sums.keys():
            equivalent_tuples = level_sums[coordinates]
            equivalent_tuples.sort(key = lambda x: x[2])
            nq.append(equivalent_tuples[0])
        q = nq
        steps += 1

    final_sum = min(sums)

    return final_sum

def minPathSumEditorial(A):
    ''' DP solution keeping only one row of state
        Time complexity is O(size(A))
        Space complexity is O(number of columns)
    '''

    if not A:
        return 0

    m, n = len(A), len(A[0])
    state = [INF] * n   # INF so 'from up' won't be chosen at first row.
    state[0] = 0        # Exception: we need to enter the first cell.
    for row in A:
        cur = INF       # INF so 'from left' won't be chosen at first col.
        for i, x in enumerate(row):
            # Best: chose among 'from left' (cur) and 'from up' (state[i])
            cur = min(cur, state[i]) + x
            state[i] = cur

    return state[-1]
