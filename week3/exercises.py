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


# INTERVIEWS
