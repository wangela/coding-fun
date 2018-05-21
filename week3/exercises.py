# TREES
## Traversal
### Inorder Traversal
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(A):
    # Parameters: A is the root node of a binary tree.
    # Perform: Traverse the tree inorder. Recursion is not allowed. Left, Root, Right
    # Return: An array of the inorder traversal of the tree nodes' values.
    # Example: 1
    #           \
    #            2
    #           /
    #          3
    #   returns [1, 3, 2]
    traversal = []
    tempStack = []
    curr_root = A
    left = A.left
    right = A.right
    done = False


    if curr_root == None:
        if len(tempStack) == 0:
            return tempStack
    else:
        while done == False:
            if curr_root != None:
                tempStack.append(curr_root)
                left = curr_root.left
                curr_root = left
            else:
                if len(tempStack) > 0:
                    curr_root= tempStack.pop()
                    traversal.append(curr_root.val)
                    right = curr_root.right
                    curr_root = right
                else:
                    done = True

    return traversal

### Postorder Traversal
def postorderTraversal(A):
    # Parameter: A is the root node of a Tree
    # Output: Return a list of integers in postorder traversal order of the Tree
    #   Left, Right, Root
    # Example:
    #       1
    #        \
    #         2
    #        /
    #       3
    #   returns [3,2,1]
    traversal = []
    tempStack = []
    curr_root = A
    done = False

    if curr_root == None:
        if len(tempStack) == 0:
            return traversal
    else:
        while done == False:
            if curr_root != None:
                if curr_root.right != None:
                    tempStack.append(curr_root.right)
                tempStack.append(curr_root)
                left = curr_root.left
                curr_root = left
            else:
                if len(tempStack) > 0:
                    curr_root = tempStack.pop()
                    right = curr_root.right
                    if right != None and len(tempStack) > 0:
                        next_root = tempStack.pop()
                        if next_root == right:
                            tempStack.append(curr_root)
                            curr_root = right
                        else:
                            tempStack.append(next_root)
                            traversal.append(curr_root.val)
                            curr_root = None
                    else:
                        traversal.append(curr_root.val)
                        curr_root = None
                else:
                    done = True

    return traversal


## Level Order
### Populate Next Right Pointers Tree
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    # Parameter: The root node of a binary tree
    # Perform: Populate the next pointer to point to the next right node. If no
    #   next right node, set next pointer to None.
    # Output: Nothing
    # Goal: O(1) extra space. Recursion is not constant space. The binary tree
    #   may not be perfect.
    # 387077 340383 562082 409269 517606 534779 986434 702531 720965 647033 727076 NULL 719463 983736 824451 834145 NULL NULL NULL NULL NULL
    # 387077 340383 562082 409269 517606 534779 986434 702531 720965 647033 727076 NULL 719463 983736 824451 834145 NULL NULL NULL NULL NULL
    # 28853 33090 26527 100198 161326 180722 87854 50782 51208 69725 66899 103548 79117 73260 134531 114761 664467 326663 850082 196521 187605 255457 298159 603123 415961 411487 412294 NULL NULL 377684 209762 274844 379623 311604 344728 545464 357548 773985 462110 548587 398392 477976 468700 492019 498100 491819 599430 507966 585788 509566 NULL NULL 610117 NULL 604554 603382 602218 619311 616193 760369 633869 678183 NULL 684882 646060 671177 667529 973809 681109 689824 762219 747257 NULL 773186 784081 826902 780090 776851 899271 792094 831066 NULL NULL 862205 868662 NULL NULL 959993 951588 976568 NULL NULL NULL NULL
    # 28853 33090 26527 100198 161326 180722 87854 50782 51208 69725 66899 103548 79117 73260 134531 114761 664467 326663 850082 196521 187605 255457 298159 603123 415961 411487 412294 NULL NULL 377684 209762 274844 379623 311604 344728 545464 357548 773985 462110 548587 398392 477976 468700 492019 498100 491819 599430 507966 585788 509566 NULL NULL 610117 NULL 604554 603382 602218 619311 616193 760369 633869 678183 NULL 684882 646060 671177 667529 973809 681109 689824 762219 747257 NULL 773186 784081 826902 780090 776851 899271 792094 831066 NULL NULL 862205 868662 NULL NULL 959993 951588 976568 NULL NULL NULL NULL

    current_node = root
    first_next = None
    last_next = None
    while current_node:
        current_left = current_node.left
        current_right = current_node.right
        if current_left and not first_next:
            print("A")
            first_next = current_left
        if current_left and last_next:
            print("B")
            last_next.next = current_left
            last_next = current_left
        elif current_left and not last_next:
            print("B2")
            last_next = current_left
        if current_left and current_right:
            print("C")
            current_left.next = current_right
            last_next = current_right
        if current_right and not first_next:
            print("D")
            first_next = current_right
        if current_right and last_next:
            print("E")
            last_next.next = current_right
            last_next = current_right
        if current_node.next:
            print("F")
            current_node = current_node.next
        else:
            print("G")
            current_node = first_next
            first_next = None
            last_next = None

    return root

## Simple Tree Ops
### Balanced Binary Tree
def getHeight(A):
    left_height = 0
    right_height = 0
    curr_root = A
    if curr_root != None:
        left_root = curr_root.left
        right_root = curr_root.right
        if left_root != None:
            left_height += 1
            left_height += getHeight(left_root)
        if right_root != None:
            right_height += 1
            right_height += getHeight(right_root)
    height = max(left_height, right_height)

    return height

def isBalanced(A):
    # Parameters: A is the root node of a binary tree
    # Perform: Height-balanced means the depth of the two subtrees of every node
    #   never differs by more than 1
    # Output: Return an integer 1 if True or 0 if False if this tree is height-balanced
    # Example:
    #           1
    #          / \
    #         2   3
    #   Returns 1
    left_height = 0
    right_height = 0
    curr_root = A

    if curr_root == None:
        return 0                # Check this with test input
    else:
            left_root = curr_root.left
            left_height = getHeight(left_root)
            right_root = curr_root.right
            right_height = getHeight(right_root)
            if abs(left_height - right_height) > 2:
                return 0
            if (self.isBalanced(left_root) and self.isBalanced(right_root)):
                return 1
            else:
                return 0


## 2 Trees
### Identical Binary Tree
def inorderTraversal(A):
    traversal = []
    curr_root = A

    if curr_root != None:
        left = curr_root.left
        right = curr_root.right
        traversal.append(inorderTraversal(left))
        traversal.append(curr_root.val)
        traversal.append(inorderTraversal(right))

    return traversal

def isSameTree(A, B):
    # Parameters: A and B are root nodes of binary trees
    # Output: 0 if false or 1 if true if binary trees are structurally identical and have nodes of hte same values
    traversalA = []
    traversalB = []

    traversalA = inorderTraversal(A)
    traversalB = inorderTraversal(B)

    if traversalA == traversalB:
        return 1
    else:
        return 0


## Root to Leaf
### Max Depth of Binary Tree
def maxDepth(A):
    max_height = 0
    curr_root = A
    left_height = 0
    right_height = 0

    if curr_root != None:
        left = curr_root.left
        right = curr_root.right
        left_height = maxDepth(left)
        right_height = maxDepth(right)
        max_height = max(left_height, right_height) + 1

    return max_height


## Inplace Change
### Invert the Binary Tree
def invertTree(root):
    # Parameters: A is the root node of a binary tree
    # Output: Return the root node of the inverted binary tree
    if root != None:
        left = root.left
        right = root.right
        root.left = invertTree(right)
        root.right = invertTree(left)

    return root



# HEAPS
## Heap
### Magician and Chocolates
def nchoc(A, B):
    # Parameters:
    #   A is an integer, the units of time the kid will have to eat chocolates
    #   B is a list of integers, the number of choclates in each bag of candy
    # Output:
    #   Return an integer, the maximum number of chocolates the kid can eat
    #   Return answer modulo 10^9 + 7
    import heapq
    import math

    eat = 0
    mirrorB = []

    for each in B:
        x = int(math.copysign(each, -1))
        mirrorB.append(x)

    heapq.heapify(mirrorB)

    while A > 0:
        if len(mirrorB) > 0:
            most_chocolate = int(math.copysign(heapq.heappop(mirrorB), 1))
            eat += most_chocolate
            half_chocolate = most_chocolate // 2
            if half_chocolate > 0:
                negative_chocolate = int(math.copysign(half_chocolate, -1))
                heapq.heappush(mirrorB, negative_chocolate)
        else:
            break
        A -= 1

    mostest = 10**9 + 7
    remainder = eat % mostest
    return remainder


### N max pair combinations
import heapq
def solve(A, B):
    # Parameters: A, B are lists of integers, both of size N
    # Perform: Find the maximum N elements from the sum combinations (Ai + Bj)
    # Output: A list of integers
    # Example: [1, 4, 2, 3] and [2, 5, 1, 6] -> [4 + 6, 3 + 6, 4 + 5, 2 + 6] -> [10, 9, 9, 8]
    # Approach: Sort the input lists descending,
    #   Add the sum of largest two elements from each list to a max heap,
    #   Then for N times pop the top of the heap and push on the next two sums
    #   (incrementing index of each list by one), making sure the combinations
    #   of indices hasn't already been added before.

    h = []
    answer = []
    n = len(A)
    if n == 0:
        return []
    visited = set()
    negative_a = [-x for x in A]    # negate because heapq is a min heap and we need a max heap
    negative_b = [-x for x in B]
    sorted_a = sorted(negative_a)
    sorted_b = sorted(negative_b)
    t = (sorted_a[0] + sorted_b[0], (0, 0))
    visited.add(t[1])
    heapq.heappush(h, t)

    for x in range(n):
        top = heapq.heappop(h)
        top_value = top[0]
        top_lefti = top[1][0]
        top_rightj = top[1][1]
        push_lefti = top_lefti + 1
        push_rightj = top_rightj + 1
        if push_lefti >= n:
            push_lefti = top_lefti
        if push_rightj >= n:
            push_rightj = top_rightj
        left_coordinates = (push_lefti, top_rightj)
        right_coordinates = (top_lefti, push_rightj)

        answer.append(-top_value)   # negate when we add to the answer to restore to positive
        if left_coordinates not in visited:
            visited.add(left_coordinates)
            t = (sorted_a[left_coordinates[0]] + sorted_b[left_coordinates[1]], left_coordinates)
            heapq.heappush(h, t)
        if right_coordinates not in visited:
            visited.add(right_coordinates)
            t = (sorted_a[right_coordinates[0]] + sorted_b[right_coordinates[1]], right_coordinates)
            heapq.heappush(h, t)

    return answer


### Merge K sorted lists
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(A):
    # Input: A is a list of sorted linked lists
    # Perform: Merge the multiple linked lists into a single sorted linked list
    # Output: Return the head of a linked list
    # Example: [1, 10, 20], [4, 11, 13], [3, 8, 9] -> [1, 3, 4, 8, 9, 10, 11, 13, 20]
    h = []
    k = len(A)
    answer = ListNode(None)

    for i in range(k):
        curr_list_node = A[i]
        while curr_list_node != None:
            curr_value = curr_list_node.val
            next_node = curr_list_node.next
            heapq.heappush(h, curr_value)
            curr_list_node = next_node

    if len(h) > 0:
        answer.val = heapq.heappop(h)
        last_node = answer

    while len(h) > 0:
        last_node.next = ListNode(heapq.heappop(h))
        last_node = last_node.next

    return answer


## Heap Math
### Ways to Form Max Heap
def solve(A):
    # Parameter: A is an integer, A <= 100
    # Perform: Determine how distinct max heaps can be made from n distinct integers
    # Output: An integer, modulo 1000000007
    # Example: 4 distinct integers -> 3 distinct max heaps





## Heapmap
### Distinct Numbers in Window
def dNums(A, B):
    # Parameters:
    #   A is a list of integers
    #   B is an integer
    # Output:
    #   Return a list of integers, size N-B+1 where the ith element contains the
    #   number of distinct elements in sequence Ai, Ai+1, ... Ak+1
    # Example:
    #   [1, 2, 1, 3, 4, 3] and B = 3 -> [2, 3, 3, 2]
    # Approach:
    #   Naive:
    #   For each index in the result list (length is 0 to len(A) - B):
    #       Create the subarray of length B
    #       For each element try adding it to a set
    #       If unique to set increment counter for that
    #       Append the counter to the result list
    #   Efficient:
    #   For each element in A:
    #       Maintain a dictionary of frequency of character in the Window
    uniqueCounts = []
    uniques = {}
    i = 0

    sub_list = A[i:(i + B)]
    for each in sub_list:
        if each in uniques:
            uniques[each] += 1
        else:
            uniques[each] = 1
    uniqueCounts.append(len(uniques))

    while i <= (len(A) - B - 1):
        character = A[i]
        character_count = uniques[character]
        if character_count == 1:
            uniques.pop(character, None)
        else:
            uniques[character] -= 1
        next = A[i + B]
        if next in uniques:
            uniques[next] += 1
        else:
            uniques[next] = 1
        uniqueCounts.append(len(uniques))
        i += 1

    return uniqueCounts


# BINARY SEARCH
## Simple Binary Search
### Sorted Insert Position
def searchInsert(A, B):
    # Parameters:
    #   A is a sorted array with no duplicates
    #   B is an integer, a target value
    # Output: An integer, the index if the target is found. If the target is not
    #   found, the index if the target were inserted
    # Examples:
    #   [1, 3, 5, 6], 5 -> 2
    #   [1, 3, 5, 6], 2 -> 1
    #   [1, 3, 5, 6], 0 -> 0
    #   [1, 3, 5, 6], 7 -> 4
    length = len(A)
    if length == 1:
        value = A[0]
        if value < B:
            return 1
        else:
            return 0
    elif length == 2:
        value = A[0]
        max_val = A[1]
        if max_val < B:
            return 2
        elif value < B and B <= max_val:
            return 1
        else:
            return 0

    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        curr = A[mid]
        if curr == B:
            return mid
        elif curr < B:
            left = mid + 1
        elif curr > B:
            right = mid - 1

    return left


## Search Answer
### Square Root of Integer
def sqrt(A):
    # Parameter: A is an integer
    # Perform: Calculate the square root without using sqrt from standard library
    # Output: Return the square root of the integer. If x is not a perfect
    #   square, return floor(sqrt(x))
    # Example: 11 -> 3
    # Approach:
    #   Is there an upper bound for A?
    #   Construct a list of squares up to sys.maxint
    left = 0
    right = A
    while left <= right:
        r = (left + right) // 2
        square = r**2
        if square == A:
            return r
        elif square < A:
            left = r + 1
        elif square > A:
            right = r - 1
    left -= 1
    return left


    return root



# CHALLENGES
class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

INT_MAX = sys.maxint # 9223372036854775807
INT_MIN = -sys.maxint - 1 # -9223372036854775808

def isBST(root_node):
    return isBSTUtil(root_node, INT_MIN, INT_MAX)

def isBSTUtil(node, mini, maxi):
    # Parameter: A TreeNode representing the root of a tree
    # Output: A boolean True if the tree is a BST and False if the tree is not
    # BST rules:
    #   self.left.value <= self.value and self.value < self.right.value
    #   Any duplication allowed?
    #   For root, min and max are integer bounds
    #   For left of root, min is min integer but max is root value
    #   For right of root, min is root value and max is max
    if not node:   # have hit None
        return True
    node_value = node.value
    if node_value < mini or node_value > maxi:
        return False
    if isBSTUtil(left_node, mini, node_value-1) and isBST(right_node, node_value + 1, maxi):  # Recursively check following values
        return True
    else:
        return False

def count_leaves(node):
    # Parameter: A TreeNode representing the root of a tree
    # Output: An integer representing the number of nodes with no children
    if node == None:
        return 0
    left_node = node.left
    right_node = node.right
    if node.left == None and node.right == None:
        return 1
    else:
        sum_leaves = count_leaves_util(left_node) + count_leaves_util(right_node)
        return sum_leaves

def compare_trees(tree1node, tree2node):
    if tree1node == None and tree2node == None:
        return True
    elif tree1node != None and tree2node != None:
        if tree1node.value == tree2node.value:
            return (compare_trees(tree1node.left, tree2node.left) and compare_trees(tree1node.right, tree2node.right))
        else:
            return False
    else:
        return False

def golden_leaf(node, target):
    # Parameters: root is the root of a binary tree and target is an integer
    # Perform: Calculate the sum of all nodes along the path from root to each leaf
    # Hint: Use a breadth-first search
    # Output: A boolean True if the tree contains such a path, False if the tree does not
    # Approach:
    #   Am I a leaf?
    #       Yes: Adding me equal to target?
    #       No: Adding me less or equal to target?
    #           Yes: Try my left and right nodes
    #           No: Quit
    if not node:
        return False
    target = target - node.value
    if not node.left and not node.right:
        if target == 0:
            return True
        else:
            return False
    else:
        if target > 0:
            return (sum_nodes(node.left, target) or sum_nodes(node.right, target))
        else:
            return False

def golden_path(node, target):
    # Parameters: root is the root of a binary tree and target is an integer
    # Perform: Calculate the sum of all nodes along the path from root to each leaf
    # Hint: Use a depth-first search
    # Output: A list of lists of integers containing the node values of all paths to golden leaves
    # Approach:
    #   Am I a leaf?
    #       Yes: Adding me equal to target?
    #           Yes: Append my list to the answer
    #           No: Forget my list
    #       No: Adding me less or equal to target?
    #           Yes:    Append me to the list and pass it to left and right
    #           No: Forget my list
    answer = []

def recurse_path(node, target):


# Simple Search
def searchRange(A, B):
    # Parameters: A is a tuple of sorted integers, B is an integer
    # Perform: Find the starting and ending index of the target value
    # Return: A list of integers representing the starting and ending indices of the integer.
    #   If not found, return [-1, -1]
    # Goal: Runtime complexity must be O(log n)
    # Example: [5, 7, 7, 8, 8, 10], 8 -> [3, 4]
    length = len(A)
    answer = [-1, -1]
    if length == 0:
        return answer
    start = 0
    end = length - 1
    while start < end:
        mid = (start + end) // 2
        if A[mid] == B:
            end = mid
        elif A[mid] < B:
            start = mid + 1
        else: # A[mid] > B
            end = mid - 1
    if A[start] != B:
        return answer
    answer[0] = start
    end = length - 1
    while start < end:
        mid = (start + end + 1) // 2
        if A[mid] == B:
            start = mid
        else: # A[mid] > B
            end = mid - 1
    answer[1] = start
    return answer

## Traversal
### Vertical Order Traversal

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def votHelper(A, left_col, mid_col, right_col, level):
    answer = []
    if A.left != None:
        votHelper([], left_col, mid_col)
    mid_col.insert(A.val)
    if A.right != None:
        votHelper(mid_col, right_col, [])

    return answer

from collections import deque
def verticalOrderTraversal(A):
    # Parameter: A is the root node of a binary tree
    # Perform: If two tree nodes share the same vertical line, the one with lesser depth comes first
    # Output: Return a list of lists of integers (each sublist is a vertical line)
    # Approach: Hashmap for each column
    answer = []

    columns = {}
    q = deque([])
    nextq = deque([])
    if A == None:
        return []
    else:
        q = deque([(0, A)])
        min_col = 0
        max_col = 0

    while q:
        current = q.popleft()
        current_col = current[0]
        current_node = current[1]
        current_val = current_node.val
        current_left = current_node.left
        current_right = current_node.right
        if current_col in columns:
            current_col_list = columns[current_col]
            current_col_list.append(current_val)
            columns[current_col] = current_col_list
        else:
            columns[current_col] = [current_val]
        if current_left != None:
            left_col = current_col - 1
            min_col = min(left_col, min_col)
            nextq.append((left_col, current_left))
        if current_right != None:
            right_col = current_col + 1
            max_col = max(right_col, max_col)
            nextq.append((right_col, current_right))
        if not q:
            q = nextq
            nextq = deque([])

    for column in range(min_col, max_col + 1):
        answer.append(columns[column])

    return answer



### Sum Root to Leaf Numbers
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def produceNum(A):
    # Parameter: A list of nodes containing the digits in a number
    # Output: A number comprised of those digits
    power = 1
    answer = 0
    for each_node in reversed(A):
        digit = each_node.val
        answer += digit * power
        power *= 10

    return answer

def sumNumbers(A):
    # Parameter: Root node of a binary tree where each node is a digit 0-9
    # Perform: Sum all the root-to-leaf paths % 1003
    # Output: The sum
    q = []
    q.append([A])
    sum = 0

    while q:
        curr_list = q.pop()
        last_node = curr_list[-1]
        if !last_node.left and !last_node.right:        # reached a leaf
            curr_num = produceNum(curr_list)
            sum += curr_num
            sum %= 1003
        if last_node.left:
            left_list = list(curr_list)
            left_list.append(last_node.left)
            q.append(left_list)
        if last_node.right:
            right_list = list(curr_list)
            right_list.append(last_node.right)
            q.append(right_list)

    return sum

## BINARY SEARCH
### Implement Power Function
def pow(x, n, d):
    # Parameters: x is an integer, n is an integer representing the exponent,
    #   and d is an integer to modulo the exponential result (show the remainder)
    # Perform: Apply (x ^ n) % d and since the remainder cannot be negative
    # Output: The remainder after modulo. Do not return a negative answer
    # Example: x = 2, n = 3, d = 3 -> 2 % 3 = 8 % 3 = 2 -> 2
    m = x % d
    if n == 0:
        if x == 0:
            return 0
        else:
            return 1
    elif n == 1:
        return m
    else:
        r = n % 2
        m = n // 2
        if r == 0:
            answer = pow(x * x, m, d)
        else:
            answer = x * pow(x * x, m, d)
        answer %= d

    return answer
