# GRAPHS
## Graph Traversal
### Level Order
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def levelOrder(A):
        # Parameter: A is the root node of a binary tree
        # Output: Return a list of a list of integers
        # Example: Output [ [3], [9, 20], [15, 7] ]
        answer = []
        current_node = A
        current_level = 0
        current_pair = []
        node_queue = deque([[A, current_level]])
        while len(node_queue) > 0:
            current_pair = node_queue.popleft()
            current_node = current_pair[0]
            current_level = current_pair[1]
            if current_node.left:
                next_level = current_level + 1
                node_queue.append([current_node.left, next_level])
            if current_node.right:
                next_level = current_level + 1
                node_queue.append([current_node.right, next_level])
            if current_level + 1 > len(answer):
                answer.append([current_node.val])
            else:
                answer[current_level].append(current_node.val)
        return answer


### Stepping Numbers
def stepnum(A, B):
    # Parameters: A and B are Numbers
    # Perform: Stepping numbers are stepping if the adjacent digits have a difference of 1
    # Output: Find all stepping numbers in range A to B
    # Example: N = 10, M = 20 -> 10, 12
    #       N = 10, M = 23 -> 10, 12, 21, 23
    #       N = 8, M = 123 -> 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78. 87. 89. 98, 101, 121, 123
    answer = []
    for x in range(10):
        for y in generate_steps(A, B, x):
            answer.append(y)
    answer.sort()
    return answer

def generate_steps(A, B, x):
    result = []
    all_stepping_numbers = deque([])
    all_stepping_numbers.append(x)
    while len(all_stepping_numbers) > 0:
        current_num = all_stepping_numbers.popleft()
        if current_num >= A and current_num <= B:
            result.append(current_num)
        if current_num == 0 or current_num > B:
            continue

        last_digit = current_num % 10
        step_down = current_num * 10 + (last_digit - 1)
        step_up = current_num * 10 + (last_digit + 1)

        if last_digit == 0:
            all_stepping_numbers.append(step_up)
        elif last_digit == 9:
            all_stepping_numbers.append(step_down)
        else:
            all_stepping_numbers.append(step_down)
            all_stepping_numbers.append(step_up)
    return result

## Shortest Path
### Sum of Fibonacci Numbers
def fibsum(A):
    # Parameters: A is a target number
    # Perform: Using Fibonacci numbers, determine the minimum set of Fibonacci numbers
    #   (can repeat) to achieve the target sum of A
    # Output: A number (the minumum number of Fibonacci numbers)
    sum_stack = []
    fibs = highest_fib(A)
    largest = fibs[len(fibs) - 1]
    sum_stack.append(largest)
    A -= largest
    while A > 0:
        largest = next_highest(A, fibs)
        #print("subtracting", largest)
        sum_stack.append(largest)
        A -= largest
    return len(sum_stack)

def highest_fib(A):
    fibs = [0, 1]
    fib1 = 1
    fib2 = 1
    while fib2 <= A:
        fibs.append(fib2)
        fib1, fib2 = fib2, fib1 + fib2
        print("appending", fib2)
    return fibs

def next_highest(A, fibs):
    for x in range(len(fibs), 1, -1):
        trial = fibs[x-1]
        #print("trying", trial, "vs", A)
        if trial <= A:
            return trial
    return 0

## BFS
### Smallest sequence with given primes
def solve(A, B, C, D):
    # Parameters: A, B, C are three prime numbers and D is an integer
    # Output: Find the first D smallest integers which only have A, B, and C as their prime factors
    # Example: [2, 3, 5, 5] -> {2, 3, 4, 5, 6}
    primes = [A, B, C]
    indexes = [0, 0, 0]
    answer = []
    while len(answer) < D:
        M = min(primes)
        if len(answer) == 0:
            answer.append(M)
        elif answer[-1] != M:
            answer.append(M)
        if M == primes[0]:
            primes[0] = answer[indexes[0]] * A
            indexes[0] += 1
        elif M == primes[1]:
            primes[1] = answer[indexes[1]] * B
            indexes[1] += 1
        elif M == primes[2]:
            primes[2] = answer[indexes[2]] * C
            indexes[2] += 1
    return answer

from collections import deque
def solve_inefficient(A, B, C, D):
    # Parameters: A, B, C are three prime numbers and D is an integer
    # Output: Find the first D smallest integers which only have A, B, and C as their prime factors
    # Example: [2, 3, 5, 5] -> {2, 3, 4, 5, 6}
    answer = []
    primes = [A, B, C]
    primes.sort()
    values = set()
    current_level = 1
    current_step = 0
    node_queue = deque([(primes[0], 1), (primes[1], 1), (primes[2], 1)])
    while current_level <= (D/3 + 1):
        current_pair = node_queue.popleft()
        current_node = current_pair[0]
        current_level = current_pair[1]
        for x in range(current_step, 3):
            node_queue.append((current_node * primes[x], current_level + 1))
        current_step = (current_step + 1) % 3
        if current_node in values:
            continue
        else:
            values.add(current_node)
            answer.append(current_node)
    answer.sort()
    answer = answer[:D]
    return answer
