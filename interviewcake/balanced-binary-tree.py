class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def superbalanced_binary(root):
    # Parameter: root is a BinaryTreeNode, the root node of the tree
    # Perform: Determine if the difference between the depths of any two leaf nodes is no greater than one
    # Output: return True if the leaves satisfy, False if they don't
    # Approach: Maintain a max and min depth; if difference ever becomes greater than 1, return False
    max_depth = 0
    min_depth = 0

    # Structure nodes and depths as a tuple
    s = [(root, 1)]

    # Use DFS to find leaves one at a time
    while s:
        current = s.pop()
        current_node = current[0]
        current_depth = current[1]
        if current_node.left == None and current_node.right == None:
            # leaf found
            # check depth against max and min
            if current_depth > max_depth:
                max_depth = current_depth
            if current_depth < min_depth:
                min_depth = current_depth
            if max_depth - min_depth > 1:
                return False
        if current_node.left:
            s.append((current_node.left, current_depth + 1))
        if current_node.right:
            s.append((current_node.right, current_depth + 1))

    # All leaves checked
    return True
