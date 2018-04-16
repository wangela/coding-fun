class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def color_graph(A, D):
    # Parameters: A is a node in an undirected graph with maximum degree D
    # Perform: Find a graph coloring that uses at most D + 1 colors
    # Output: The node of a now-colored graph
    # Approach: BFS and if the node doesn't have a color then assign it a color
