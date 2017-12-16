# Create a Binary Search Tree
class treeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def insert(root, key):
    counter = 1
    if (key < root.val):
        if root.left == None:
            new = treeNode(key)
            root.left = new
        else:
            counter += insert(root.left, key)
    else:
        if root.right == None:
            new = treeNode(key)
            root.right = new
        else:
            counter += insert(root.right, key)
    return counter

def createBST(keys):
    # Parameters: keys is an array of n unique integers. 1 <= n <= 2x10^5 and
    #   1 <= keys[i] <= n
    # Perform: Implement the BST algorithm
    # Output: Print the value of the counter variable on a new line after each
    #   insertion of a key into the tree
    # Examples:
    #   [2, 1, 3] returns
    #   0
    #   1
    #   2
    #   [1, 2, 3] returns
    #   0
    #   1
    #   3
    counter = 0
    tree = []

    for key in keys:
        if len(tree) > 0:
            root = tree[0]
            counter += insert(root, key)
        else:
            new = treeNode(key)
            tree.append(new)
        print counter



# Valid Binary Search Trees
# Input: first line q denotes number of queries coming 1 <= q <= 10
# 2*q subsequent lines have a query across two lines:
#   first line has an integer n denoting number of nodes in tree 1 <= n <= 100
#   second line has a list of n distinct space-separated integers describing a
#       pre-order traversal of a binary tree
# Output: For each query, print 'YES' on a new line if query describes a valid BST
#   Else, print 'NO'
# Examples:
#   [1, 3, 2] -> YES
#   [2, 1, 3] -> YES
#   [3, 2, 1, 5, 4, 6] -> YES
#   [1, 3, 4, 2] -> NO
#   [3, 4, 5, 1, 2] -> NO
# Approach:
#   For each node, minint < node.left < node.val and node.val < node.right < maxint
class treeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def constructBST(nodes, minimum, maximum):
    if nodes[0] == None:
        return None
    else:
        for index, node in nodes:
            if isValid(node, minimum, maximum):
                curr_root = treeNode(node)
                print 'YES'
                if index < nodes - 1:
                    if isValid(nodes[index + 1], minimum, curr_root.val):
                        curr_root.left = nodes[index + 1]
                        print 'YES'
                    elif isValid(nodes[index + 1], curr_root.val, maximum):
                        curr_root.right = nodes[index + 1]
                        print 'YES'
                    else:
                        print 'NO'
    return root

def isValid(node, minimum, maximum):
    if node == None:
        return True
    else:
        left = node.left
        right = node.right
        if node.val < maxiumum and node.val < minimum:
            if isValid(left, minimum, node.val) and isValid(right, node.val, maximum):
                return True
            else:
                return False
        else:
            return False

def isBST():
    q = raw_input()
    for each in range(q):
        n = raw_input()
        nodes = [int(x) for x in raw_input().split()]

    MAXINT = 9223372036854775807
    MININT = -9223372036854775808

    constructBST(nodes)


# Simple queries
def counts(nums, maxes):
    # Parameters:
    #   nums is an array of n positive integers
    #   maxes is an array of m positive integers
    # Perform:
    #   For each max in maxes, how many nums are <= max
    # Output:
    #   An array listing the number of nums <= the max in maxes
    import heapq
    heapq.heapify(nums)

    answer = []
    for max in maxes:
        count = 0
        # search for max in the nums heap
        answer.append(count)

    return answer

## Naive Approach
def counts(nums, maxes):
    # Parameters:
    #   nums is an array of n positive integers
    #   maxes is an array of m positive integers
    # Perform:
    #   For each max in maxes, how many nums are <= max
    # Output:
    #   An array listing the number of nums <= the max in maxes
    answer = []
    for max in maxes:
        count = 0
        for num in nums:
            if num <= max:
                count += 1
        answer.append(count)

    return answer
