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
    # Perform: Traverse the tree inorder. Recursion is not allowed.
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
                    traversal.append(latest.val)
                    right = curr_root.right
                    curr_root = right
                else:
                    done = True

    return traversal


## Simple Tree Ops
### Balanced Binary Tree
def getLeftHeight(A):
    height = 0
    curr_root = A
    left_root = curr_root.left
    if left_root != None:
        height += 1
        height += getLeftHeight(left_root)
    else:
        return height

def getRightHeight(A):
    height = 0
    curr_root = A
    right_root = curr_root.right
    if right_root != None:
        height += 1
        height += getRightHeight(right_root)
    else:
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
    balanced = 0
    temp_stack = []
    left_height = 0
    right_height = 0
    curr_root = A

    if curr_root == None:
        return 1                # Check this with test input
    else:
            left_height += 1
            temp_stack.append(curr_root)
            left_root = curr_root.left
            left_height = getLeftHeight(left_root)
            right_root = curr_root.right
            right_height = getRightHeight(right_root)
            if (math.abs(left_height - right_height) < 2 and isBalanced(left_root) == 1 and isBalanced(right_root) == 1):
                return 1
            else:
                return 0


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
    
