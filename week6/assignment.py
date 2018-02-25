## Simple Array DP
### Stairs
def climbStairs(A):
    # Parameters: A is an integer representing n Stairs
    # Perform: At each move you can climb either 1 or 2 steps
    # Output: An integer, the number of distinct ways you can climb to the top
    # Examples: 2 -> [1 1], [2] -> 2
    #   3 -> [1 1 1], [1 2], [2 1] -> 3
    #   4 -> [1 1 1 1], [1 1 2], [1 2 1], [2 1 1], [2 2] -> 5
    if A == 0:
        return 0
    if A == 1:
        return 1

    fib = [1, 1]

    for i in range(2, A + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[-1]


## DP Tricky
### Best Time to Buy and Sell Stocks III
def maxProfit(A):
    # Perform: Can buy and sell at most 2 times
    # Examples: [1, 2, 1, 2] -> 1 + 1 -> 2
    #   [1 2 3] -> 2
    #  [2, 3, 5, 4, 8, 3, 5, 1, 4] -> [0 1 3 3 7 7 8 8 9] -> 9
    #  [2, 3, 5, 4, 8, 3, 5, 1, 4, 2, 10, 3] -> [0 1 3 3 7 7 8 8 9 9 15, 15] -> 15
    num_days = len(A)
    maxProfits = [0] * num_days
    if num_days == 0:
        return 0

    max_price = A[-1]

    for i in range(num_days - 2, 0, -1):
        if A[i] > max_price:
            max_price = A[i]
        maxProfits[i] = max(maxProfits[i + 1], max_price - A[i])

    min_price = A[0]

    for j in range(1, num_days):
        if A[j] < min_price:
            min_price = A[j]

    maxProfits[j] = max(maxProfits[j - 1], maxProfits[j] + (A[j] - min_price))

    return maxProfits[-1]

## Tree DP
### Max Sum Path in Binary Tree
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

max_sum = -sys.maxint

def maxPathUtil(A):
    if A == None:
        return 0
    elif A.left == None and A.right == None:
        self.max_sum = max(self.max_sum, A.val)
        return A.val

    left = self.maxPathUtil(A.left)
    right = self.maxPathUtil(A.right)

    max_oneside = max(A.val, max(left, right) + A.val)

    max_together = max(max_oneside, left + right + A.val)

    self.max_sum = max(self.max_sum, max_together)

    return max_oneside

def maxPathSum(A):
    # Parameters: A is the root node of a binary tree
    # Perform: Paths may start and end at any node in the tree
    # Output: The maximum path sum
    self.max_sum = -sys.maxint

    maxPathUtil(A)
    return self.max_sum


## 2 String DP
### Edit Distance
def minDistance(A, B):
    # Parameters: A and B are words (strings).
    # Perform: Each operation is 1 step: insert a character, remove a character,
    #   or replace a character.
    # Output: Return an integer of the minimum number of steps to achieve the conversion
    # Example: Anshuman -> Anthuman -> Antihuman -> 2
    rows = len(A) + 1
    cols = len(B) + 1
    per_row = [0] * cols
    edits = []
    for n in range(rows):
        edits.append(list(per_row))

    edits[0][0] = 0

    for y in range(rows):
        edits[y][0] = y

    for x in range(cols):
        edits[0][x] = x

    for i in range(1, rows):
        for j in range(1, cols):
            if A[i - 1] == B[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = min(edits[i - 1][j], edits[i][j - 1], edits[i - 1][j - 1]) + 1

    return edits[rows - 1][cols - 1]


### Longest Increasing Subsequence
def lis(A):
    # Parameters: A is a tuple of integers
    # Output: An integer, the length of the longest increasing subsequence
    # Example: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] -> [0, 2, 6, 9, 13, 15]
    #   or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15] -> 6
    if len(A) == 0:
        return 0

    subsequences = dict()       # key = value, subsequences = the longest subsequence smaller
    max_lengths = [1] * len(A)
    subsequences[A[0]] = []

    for i in range(1, len(A)):
        current_max = 1
        max_sub = 0
        for j in range(i - 1, -1, -1):
            check = A[j]
            if check < A[i]:
                if check in subsequences:
                    j_sub = list(subsequences[check])
                    j_sub.append(check)
                    if len(j_sub) > max_sub:
                        subsequences[A[i]] = j_sub
                        max_sub = len(j_sub)
                else:
                    subsequences[A[i]] = [check]
                    max_sub = 1
        if A[i] not in subsequences:
            subsequences[A[i]] = []
        max_lengths[i] = max(max_sub + 1, max_lengths[i - 1])

    return max_lengths[-1]


## Derived DP
### Max Sum Without Adjacent Elements
def max_sum(grid):
    # Parameters: grid is a list of two lists of N integers
    # Perform: Find the maximum sum by choosing numbers that are not adjacent to
    #   each other (cannot be adjacent horizontally, vertically, or diagonally)
    # Ouptput: The maximum sum of the chosen non-adjacent numbers

    # Count columns
    n = len(grid[0])
    if n == 0:
        return 0

    # Fill the memoization array
    maxsums = [0] * n

    # Answer the first column, handle base case
    maxsums[0] = max(grid[0][0], grid[1][0])

    # Answer the first quad
    if n > 1:
        maxsums[1] = max(maxsums[0], grid[0][1], grid[1][1])

    # Answer any additional columns by comparing the last solution to the current max + the solution 2 columns ago
    if n > 2:
        for i in range(2, n):
            maxsums[i] = max(maxsums[i - 1], max(grid[0][i], grid[1][i]) + maxsums[i - 2])

    return maxsums[-1]

## Greedy or DP
### Jump Game Array
def canJump(A):
    # Parameter: A is a list of non-negative integers.
    # Perform: At each index, the integer represents the maximum jump length at that position
    # Output: An integer 1 if you are able to reach the last index, 0 if not
    # Example: [2, 3, 1, 1, 4] -> [2, 1, 1] -> 1
    #          [3, 2,1, 0, 4] -> [x, 0] -> 0
    #           [] -> 1
    #           [3] -> 1, [0] -> 1
    goal = len(A) - 1
    if goal <= 0:
        return 1
    max_landing = 0

    for index, i in enumerate(A):
        if max_landing < index:
            return 0
        max_landing = max(max_landing, index + i)
        if max_landing >= goal:
            return 1

    return 0
