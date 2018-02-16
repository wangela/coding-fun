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

// Possibility of Finishing All Courses Given Pre-requisites
func preReq_util(_ node: Int,_ graph: [Int: [Int]], _ visited: inout [Bool], _ stack: inout [Bool]) -> Bool {
    visited[node] = true
    stack[node] = true
    
    guard let children = graph[node] else { return false }
    for child in children {
        if visited[child] == false {
            if preReq_util(child, graph, &visited, &stack) {
                return true
            }
        } else if stack[child] == true {
            return true
        }
    }
    
    stack[node] = false
    return false
}

func solve(_ A: inout Int, _ B: inout [Int], _ C: inout [Int]) -> Int {
    // Parameters: A is a total number of courses needed to take. B[i] is a pre-requisite for C[i]
    // Output: 1 if possible, 0 if not possible to complete all courses
    // Example: If N = 3 and prereqs are [1, 2] and [2, 3] then 1, 2, 3 -> 1
    // Example: If N = 2 and prereqs are [1, 2] and [2, 1] then not possible -> 0
    var graphDict = [Int: [Int]]()
    var visited = [Bool]()
    var stack = [Bool]()
    
    for i in 0..<A {
        graphDict[i] = []
        visited.append(false)
        stack.append(false)
    }
    
    for j in 0..<B.count {
        let pre = B[j]
        let post = C[j]
        guard graphDict[pre] != nil else {
            return 0
        }
        graphDict[pre]!.append(post)
    }
    
    for x in 0..<A {
        if preReq_util(x, graphDict, &visited, &stack) { return 0 }
    }
    return 1
}

// Knight on Chess Board
func nextMoves(_ A: Int, _ B: Int, _ C: Int, _ D: Int) -> [[Int]] {
    let move1 = [C + 1, D + 2]
    let move2 = [C + 2, D + 1]
    let move3 = [C + 2, D - 1]
    let move4 = [C + 1, D - 2]
    let move5 = [C - 1, D - 2]
    let move6 = [C - 2, D - 1]
    let move7 = [C - 2, D + 1]
    let move8 = [C - 1, D + 2]
    var moves = [[Int]]()
    moves.append(move1)
    moves.append(move2)
    moves.append(move3)
    moves.append(move4)
    moves.append(move5)
    moves.append(move6)
    moves.append(move7)
    moves.append(move8)
    
    let movesCopy = moves
    var removals = 0
    for (index, move) in movesCopy.enumerated() {
        if move[0] > A || move[0] < 1 {
            moves.remove(at: index - removals)
            removals += 1
        } else if move[1] > B || move[1] < 1 {
            moves.remove(at: index - removals)
            removals += 1
        }
    }
    
    return moves
}

struct Square {
    let x: Int
    let y: Int
    let steps: Int
    
    init(x: Int, y: Int, steps: Int = 0) {
        self.x = x
        self.y = y
        self.steps = steps
    }
}

extension Square: Hashable {
    var hashValue: Int {
        return "\(self.x)\(self.y)".hashValue
    }
    
    static func ==(lhs: Square, rhs: Square) -> Bool {
        return lhs.x == rhs.x && lhs.y == rhs.y
    }
}

//func bfs(A: Int, B: Int, C: Int, D: Int, E: Int, F: Int) -> Int {
//    var visited = [Square: Bool]()
//    var q = [Square]()
//    let source = Square(x: C, y: D, steps: 0)
//    q.append(source)
//
//    while !q.isEmpty {
//        guard let s = q.removeFirst() else { break }
//        let x = s.x
//        let y = s.y
//        let steps = s.steps
//
//        if (x == E && y == F) { return steps }
//
//        if visited[s] == nil {
//            visited[s] = true
//
//            for i in nextMoves(A, B, x, y) {
//                let next = Square(x: i[0], y: i[1], steps: steps + 1)
//                q.append(next)
//            }
//        }
//    }
//
//    return -1
//}

func knight(_ A: inout Int, _ B: inout Int, _ C: inout Int, _ D: inout Int, _ E: inout Int, _ F: inout Int) -> Int {
    // Parameters: A, B are the size of the chess board; C, D coordinates of source point; E, F coordinates of destination point
    // Output: Integer of the minimum number of steps to reach destination or -1 if not possible
    // Example: 8, 8, 1, 1, 8, 8 -> 6
    var visited: [Square: Bool] = [:]
    var q = [Square]()
    let source = Square(x: C, y: D, steps: 0)
    q.append(source)
    
    while !q.isEmpty {
        let s = q.removeFirst()
        let x = s.x
        let y = s.y
        let steps = s.steps
        
        if (x == E && y == F) { return steps }
        
        if visited[s] == nil {
            visited[s] = true
            
            for i in nextMoves(A, B, x, y) {
                let next = Square(x: i[0], y: i[1], steps: steps + 1)
                q.append(next)
            }
        }
    }
    
    return -1
}

let input = [2, 20, 1, 18, 1, 5]
var a = input[0]
var b = input[1]
var c = input[2]
var d = input[3]
var e = input[4]
var f = input[5]
knight(&a, &b, &c, &d, &e, &f)

