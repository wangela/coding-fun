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

### Word Search board
def searchUtil(N, B, I, J):
    if len(B) == 0:
        return False
    elif len(B) == 1:
        if N[I][J] == B[0]:
            return True
    else:   # len(B) > 1:
        if searchUtil(N, B[1:], I, J):
            print(B[1:], I, J)
            neighbors = set()
            if J < len(N[0]) - 1:
                neighbors.add(N[I][J + 1])
            if J > 0:
                neighbors.add(N[I][J - 1])
            if I < len(N) - 1:
                neighbors.add(N[I + 1][J])
            if I > 0:
                neighbors.add(N[I - 1][J])
            print("neighbors = ", neighbors)
            if B[0] in neighbors:
                return True
    return False

def exist(A, B):
    # Parameters: A is a 2-D board (array of arrays) and B is a word (string)
    # Perform: Find if a word exists in the board. Word exists if it can be
    #   constructed out of letters adjacent horizontally or vertically. Letters
    #   can be used more than once.
    # Output: Return 1 if exists, 0 if doesn't exist in the board.
    # Example: [['ABCE'], ['SFCS'], ['ADEE']]
    #     "ABCCED" -> 1, "ABCB" -> 1, "ABFSAB" -> 1, "ABCD" -> 0
    # Approach: Create a bi-directional graph (adjacency list as dictionary),
    #   then recursively search the graph for the word starting with the last
    #   letter of the word
    row_length = len(A)
    col_length = len(A[0])

    for i in range(row_length):
        for j in range(col_length):
            if searchUtil(A, B, i, j):
                return 1
    return 0

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


## Graph Adhoc
### Convert Sorted List to Binary Tree
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getDepth(A):
    current_node = A
    left_node = A.left
    right_node = A.right
    height = 0

    while current_node:
        height += 1
        height += max(getDepth(left_node), getDepth(right_node))

    return height

def countListLength(A):
    current_node = A
    length = 0

    while current_node:
        length += 1
        current_node = current_node.next

    return length

def sortedListToBST_util(self,start, end):
    if start == end:
        return None
    else:
        mid = start + (end - start)/2
        left_head = sortedListToBST_util(start, mid)
        tree_head = TreeNode(self.head.val)
        tree_head.left = left_head
        self.head = self.head.next
        right_head = sortedListToBST_util(mid + 1, end)
        tree_head.right = right_head
        return tree_head

def sortedListToBST(self.head, A):
    # Parameter: A is a ListNode, the head node of a sorted singly linked list
    # Output: The head node (TreeNode) of a height-balanced BST (depth of subtrees of every node
    #      never differ by more than 1)
    # Example: A 1 -> 2 -> 3, output 2
    #                               1  3
    current_node = A
    length = countListLength(current_node)
    self.head = A
    tree_head = self.sortedListToBST_util(0, length)

    return tree_head

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


## Depth first search
### Largest Distance Between Nodes of a Tree
def bfs(node, graph_dict):
    distances = []

    for adjacent in graph_dict[node]:
        temp_stack.push()

def height(A, graph_dict):
    if A == None:
        return 0
    elif graph_dict[A] == []:
        return 1
    else:
        deepest = 0
        for each in graph_dict[A]:
            deepest = max(deepest, height(each, graph_dict))
        return deepest + 1

def diameter(A, graph_dict):
    if A == None:
        return 0
    elif graph_dict[A] == []:
        return 0
    else:
        highest1 = 0
        highest2 = 0
        for each in graph_dict[A]:
            current_height = height(each, graph_dict)
            if current_height > highest1:
                highest2 = highest1
                highest1 = current_height
            else if current_height > highest2:
                highest2 = current_height

        max_diameter = 0
        for child in graph_dict[A]:
            max_diameter = max(max_diameter, diameter(child, graph_dict))

        return max(max_diameter, highest1 + highest2 + 1)

def solve(A):
    # Parameter: A is the list of integers of an unweighted rooted tree with 2 <= A <= 40,000 nodes
    #   Tree is given as an array with nodes numbered 0 to A - 1. For P[i] each value is the
    #       number of the node's parent. The i with value -1 is the root.
    # Output: An integer, the largest distance (number of edges)  between two nodes in a tree
    # Example: [-1, 0, 0, 0, 3] -> 1 -> 0 -> 3 -> 4 -> 3
    if len(A) == 2:
        return 1
    tree = dict()
    root = -1
    for i, each in enumerate(A):
        if each == -1:
            if i in tree:
                root = i
            else:
                tree[i] = []
                root = i
            continue
        else:
            if each in tree:
                tree[each].append(i)
            else:
                tree[each] = [i]
            if i in tree:
                tree[i].append(each)
            else:
                tree[i] = [each]
    distances = []
    for v in range(len(A)):
        distances.append(-1)
    temp_stack = []
    temp_stack.append(0)
    distances[0] = 0
    while len(temp_stack) > 0:
        t = temp_stack.pop()
        for each in tree[t]:
            v = tree[t]
            if distances[v] == -1:
                temp_stack.insert(0, v)
                distances[v] = distances[t] + 1

    max_distance = 0
    furthest_node = 0
    for i, steps in enumerate(distances):
        if steps > max_distance:
            max_distance = steps
            furthest_node = i

    temp_stack = tree[furthest_node]
    distances = []
    for v in range(len(A)):
        distances.append(-1)
    distances[furthest_node] = 0

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


### Word Ladder I
from collections import deque
def ladderLength(start, end, dictV):
    # Parameters: start and end are strings, dictV is a list of strings
    # Perform: Count a step for each time you change 1 letter to get from start to end
    # Output: Integer, the number of steps
    d = {}
    q = deque([start])
    nq = deque()
    steps = 1
    diff = 0
    possible = False

    for entry in dictV:
        for index, letter in enumerate(entry):
            mod = entry[0:index] + "_" + entry[index + 1:]
            if mod in d:
                d[mod].append(entry)
            else:
                d[mod] = [entry]

    for ind, let in enumerate(end):
        mad = end[0:ind] + "_" + end[ind + 1:]
        if mad in d:
            d[mad].append(end)
            possible = True
        if let != start[ind]:
            diff += 1
    if diff == 1:
        return 2
    if not possible:
        return 0

    while len(q) > 0:
        nq = deque()
        while len(q) > 0:
            current = q.popleft()
            if current == end:
                return steps
            for i, l in enumerate(current):
                m = current[0:i] + "_" + current[i + 1:]
                if m in d:
                    nq += d[m]
        steps += 1
        q = nq

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    distance, cur, visited, lookup = 0, [beginWord], set([beginWord]), set(wordList)

    while cur:
        next_queue = []

        for word in cur:
            if word == endWord:
                return distance + 1
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + j + word[i + 1:]
                    if candidate not in visited and candidate in lookup:
                        next_queue.append(candidate)
                        visited.add(candidate)
        distance += 1
        cur = next_queue

    return 0

## INTERVIEWS
### Journey to the Moon
