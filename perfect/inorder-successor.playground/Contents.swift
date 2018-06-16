//: Playground - noun: a place where people can play

import Foundation

public class Node {
    
    private(set) public var value: Int
    private(set) public var parent: Node?
    private(set) public var left: Node?
    private(set) public var right: Node?
    
    public init(_ value: Int) {
        self.value = value
    }
    
    public convenience init(array: [Int]) {
        precondition(array.count > 0)
        self.init(array.first!)
        for v in array.dropFirst() {
            insert(v)
        }
    }
    
    public func insert(_ value: Int) {
        if value < self.value {
            if let left = left {
                left.insert(value)
            } else {
                left = Node(value)
                left?.parent = self
            }
        } else {
            if let right = right {
                right.insert(value)
            } else {
                right = Node(value)
                right?.parent = self
            }
        }
    }
    
    public func search(_ value: Int) -> Node? {
        var node: Node? = self
        while case let n? = node {
            if value < n.value {
                node = n.left
            } else if value > n.value {
                node = n.right
            } else {
                return node
            }
        }
        return nil
    }
    
}

func findMinKeyInTree(inputNode: Node) -> Node {
    var node = inputNode
    while case let left? = node.left {
        node = left
    }
    return node
}

func findInOrderSuccessor(inputNode: Node) -> Node? {
    guard let right = inputNode.right else {
        // no right child;
        // search ancestors for first ancestor that has the child as a left
        // if no ancestor has a the child as left, will return nil
        guard let a = inputNode.parent else {
            return nil
        }
        var child = inputNode
        while let parent = child.parent {
            if parent.value > child.value {
                return parent
            } else {
                child = parent
            }
        }
        
        return nil
    }
    return findMinKeyInTree(inputNode: right)
}


