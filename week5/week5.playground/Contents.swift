import Foundation

class TreeNode {
    var val: Int = 0
    var left: TreeNode?
    var right: TreeNode?
}

// Undirected edge
public struct Edge<T>: CustomStringConvertible {
    public let vertex1: T
    public let vertex2: T
    public let weight: Int
    
    public var description: String {
        return "[\(vertex1)-\(vertex2), \(weight)]"
    }
}

// Undirected weighted graph
public struct Graph<T: Hashable>: CustomStringConvertible {
    
    public private(set) var edgeList: [Edge<T>]
    public private(set) var vertices: Set<T>
    public private(set) var adjList: [T: [(vertex: T, weight: Int)]]
    
    public init() {
        edgeList = [Edge<T>]()
        vertices = Set<T>()
        adjList = [T: [(vertex: T, weight: Int)]]()
    }
    
    public var description: String {
        var description = ""
        for edge in edgeList {
            description += edge.description + "\n"
        }
        return description
    }
    
    public mutating func addEdge(vertex1 v1: T, vertex2 v2: T, weight w: Int) {
        edgeList.append(Edge(vertex1: v1, vertex2: v2, weight: w))
        vertices.insert(v1)
        vertices.insert(v2)
        
        adjList[v1] = adjList[v1] ?? []
        adjList[v1]?.append((vertex: v2, weight: w))
        
        adjList[v2] = adjList[v2] ?? []
        adjList[v2]?.append((vertex: v1, weight: w))
    }
    
    public mutating func addEdge(_ edge: Edge<T>) {
        addEdge(vertex1: edge.vertex1, vertex2: edge.vertex2, weight: edge.weight)
    }
}

/*
 Union-Find Data Structure
 Performance:
 adding new set is almost O(1)
 finding set of element is almost O(1)
 union sets is almost O(1)
 */

public struct UnionFind<T: Hashable> {
    private var index = [T: Int]()
    private var parent = [Int]()
    private var size = [Int]()
    
    public init() {}
    
    public mutating func addSetWith(_ element: T) {
        index[element] = parent.count
        parent.append(parent.count)
        size.append(1)
    }
    
    private mutating func setByIndex(_ index: Int) -> Int {
        if parent[index] == index {
            return index
        } else {
            parent[index] = setByIndex(parent[index])
            return parent[index]
        }
    }
    
    public mutating func setOf(_ element: T) -> Int? {
        if let indexOfElement = index[element] {
            return setByIndex(indexOfElement)
        } else {
            return nil
        }
    }
    
    public mutating func unionSetsContaining(_ firstElement: T, and secondElement: T) {
        if let firstSet = setOf(firstElement), let secondSet = setOf(secondElement) {
            if firstSet != secondSet {
                if size[firstSet] < size[secondSet] {
                    parent[firstSet] = secondSet
                    size[secondSet] += size[firstSet]
                } else {
                    parent[secondSet] = firstSet
                    size[firstSet] += size[secondSet]
                }
            }
        }
    }
    
    public mutating func inSameSet(_ firstElement: T, and secondElement: T) -> Bool {
        if let firstSet = setOf(firstElement), let secondSet = setOf(secondElement) {
            return firstSet == secondSet
        } else {
            return false
        }
    }
}

// GRAPHS
// BFS
// Level Order
func levelOrder(_ A: TreeNode?) -> [[Int]] {
    var traversal = [[Int]]()
    var levelStack = [TreeNode]()
    var nextLevel = [TreeNode]()
    var currLevel = [Int]()
    if let A = A {
        levelStack.append(A)
    } else {
        return [[]]
    }
    
    while !levelStack.isEmpty {
        let currNode = levelStack.removeFirst()
        currLevel.append(currNode.val)
        if let left = currNode.left {
            nextLevel.append(left)
        }
        if let right = currNode.right {
            nextLevel.append(right)
        }
        if levelStack.isEmpty {
            traversal.append(currLevel)
            levelStack = nextLevel
            currLevel = []
            nextLevel = []
        }
    }
    
    return traversal
}

// Graph Connectivity
// Commutable Islands
func solve(_ A: inout Int, _ B: inout [[Int]]) -> Int {
    // Parameters: A is the number of islands, B is a list of bridges denoted by [origin, destination, cost]
    // Output: An integer, the minimum cost of connecting all the islands
    var cost = Int()
    var tree = Graph<Int>()
    var unionFind = UnionFind<Int>()
    for vertex in 1...A {
        unionFind.addSetWith(vertex)
    }
    
    var edges: [Edge<Int>] = [Edge<Int>]()
    for bridge in B {
        let bedge = Edge(vertex1: bridge[0], vertex2: bridge[1], weight: bridge[2])
        edges.append(bedge)
    }
    
    let sortedEdgeListByWeight = edges.sorted(by: { $0.weight < $1.weight })
    for edge in sortedEdgeListByWeight {
        let v1 = edge.vertex1
        let v2 = edge.vertex2
        
        if !unionFind.inSameSet(v1, and: v2) {
            cost += edge.weight
            tree.addEdge(edge)
            
            unionFind.unionSetsContaining(v1, and: v2)
        }
    }
    
    return cost
}
