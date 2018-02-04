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

## Graph Connectivity
### Commutable Islands
from collections import deque
class Island:
    def __init__(self, x):
        self.id = x
        self.bridges = set()

    def add_bridge(self, y):
        self.bridges.add(y)

    def copy(self):
        new_island = Island(self.id)
        new_island.bridges = self.bridges.copy()
        return new_island

class Bridge:
    def __init__(self, x, y):
        self.destination = x
        self.cost = y

def solve(A, B):
    cost = 0
    B.sort(key = lambda x: x[2])
    islands = {}
    forest = set()
    bridges = []
    bridge_id = 0
    for island_index in range(A):
        islands[island_index] = (9223372036854775807, "flag", []) # C = maxint, E = "flag"
    for bridge in B:
        start = islands[bridge[0] - 1]
        end = islands[bridge[1] - 1]
        start[2].append((bridge[1] - 1, bridge[2]))
        end[2].append((bridge[0] - 1, bridge[2]))
        if bridge[2] < start[0]:
            c = bridge[2]
            start[0] = c
            if start[1] != "flag":
                e = bridge
                start[1] = e
        for
    first_island = B[0][0]
    forest.add(first_island)
    first_island_bridges = islands[first_island]
    while len(islands) > 0:
        first_island_bridges.sort(key = lambda x: x[1])
        for bridge in first_island_bridges:
            if bridge[0] in islands:
                print("bridge to", bridge[0], "for", bridge[1])
                cost += bridge[1]
                next_island = bridge[0]
                first_island_bridges = islands.pop(next_island)
                break
            else:
                continue
    return cost

def solve_partial(A, B):
    # Parameters: A is an integer, the number of islands. B is a list of lists of integers,
    #       representing bridges.  Each list has 3 integers where B[i][0] and B[i][1] are
    #       the two islands connected by the bridge and B[i][2] is the cost of crossing
    #       that bridge.
    # Output: The minimum cost of bridges to connect all the islands
    # Example: solve(4, [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]) ->
    #       select B[0] + B[2] + B[3] to connect all the islands for a cost of 1 + 3 + 2 = 6
    #       -> 6
    cost = 0
    B.sort(key = lambda x: x[2])
    islands = []
    needPaths = set()
    bridges = set()
    bridge_id = 0
    for island_index in range(A):
        new_island = Island(island_index)
        islands.append(new_island)
        needPaths.add(island_index)
    needPaths.remove(0)
    for bridge in B:
        needed_bridge = False
        if len(needPaths) == 0:
            return cost
        stash_start = islands[bridge[0] - 1]
        stash_end = islands[bridge[1] - 1]
        temp_start = islands[bridge[0] - 1].copy()
        temp_end = islands[bridge[1] - 1].copy()
        temp_start.add_bridge(islands[bridge[1] - 1])
        temp_end.add_bridge(islands[bridge[0] - 1])
        islands[bridge[0] - 1] = temp_start
        islands[bridge[1] - 1] = temp_end
        first_island = islands[0]
        bridge_id += 1
        print("bridge" + str(bridge_id))
        for index in needPaths.copy():
            current_island = islands[index]
            if hasPathBFS(first_island, current_island):
                needPaths.remove(index)
                print(str(index) + "no longer needs paths")
                if bridge_id not in bridges:
                    bridges.add(bridge_id)
                    cost += bridge[2]
                    needed_bridge = True
                if len(needPaths) == 0:
                    return cost
        if not needed_bridge:
            islands[bridge[0] - 1] = stash_start
            islands[bridge[1] - 1] = stash_end
    return "no solution found"

def hasPathBFS(start, destination):
    visit_list = deque([start])
    visited = set()
    visit_list.append(start)
    while len(visit_list) > 0:
        current_island = visit_list.popleft()
        if current_island == destination:
            return True
        if current_island in visited:
            continue
        visited.add(current_island)

        for child in current_island.bridges:
            visit_list.append(child)
    return False


## CHALLENGES
### Capture Regions on Board
def Location:
    def __init__(self, n, e, s, w):
        self.north = n
        self.east = e
        self.south = s
        self.west = w

def capture_regions(board):
    # Parameters: board is a 2D matrix where every location is an X or an O
    # Output: Return the same board where for every location in a region
    #   surrounded by X's, flip the location to O



## INTERVIEWS
### Journey to the Moon
