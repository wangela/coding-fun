from collections import deque

def fib(n):
    # Parameters: n is an integer
    # Output: An integer, the nth Fibonacci number in a 0-indexed Fibonacci sequence
    # Examples:
    #   0 -> 0
    #   1 -> 1
    #   2 -> 1
    #   3 -> 2
    #   4 -> 3
    #   5 -> 5
    sum = 0

    prev = deque([0, 1])
    for i in range(n+1):
        sum += prev.popleft()
        prev.append(sum)

    return sum

# O(n) time and O(1) space

# i = 3
# sum = 5
# prev = [3, 5]
