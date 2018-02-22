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
        self.max_sum = A.val
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
def editDistance(A, index_a, B, index_b):
    if A[index_a] == B[index_b]:
        return editDistance(A, index_a + 1, B, index_b + 1)
    else:
        insertion_dist = 1 + editDistance(A, index_a, B, index_b + 1)
        deletion_dist = 1 + editDistance(A, index_a + 1, B, index_b)
        replace_dist = 1 + editDistance(A, index_a + 1, B, index_b + 1)
        return min(insertion_dist, deletion_dist, replace_dist)

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
