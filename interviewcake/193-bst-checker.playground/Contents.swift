//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

class BinaryTreeNode {
    
    var value: Int
    var left: BinaryTreeNode?
    var right: BinaryTreeNode?
    
    init(_ value: Int) {
        self.value = value
    }
    
    func insert(leftValue: Int) -> BinaryTreeNode {
        let left = BinaryTreeNode(leftValue)
        self.left = left
        return left
    }
    
    func insert(rightValue: Int) -> BinaryTreeNode {
        let right = BinaryTreeNode(rightValue)
        self.right = right
        return right
    }
}

// BST rules:
// all values under left branch are less than parent value
// all values under right branch are more than parent value

// Approach:
// track max/min range of possible values
// For left branch, min is min int and max is parent value
// For right branch, max is max int and min is parent value
// As you go, max and min narrow based on min/max of the parent. Add any children to the stack (DFS)
// When you've reached the end of the stack, if you haven't failed out, return True
func checkNode(n: BinaryTreeNode? = nil, min: Int, max: Int) -> Bool {
    if let current = n {
        if (current.value < min || current.value > max) {
            return false
        }
        
        return checkNode(n: current.left, min: min, max: current.value - 1) && checkNode(n: current.right, min: current.value + 1, max: max)
        
    } else {
        return true
    }
}

func checkBST(root: BinaryTreeNode) -> Bool {
    return checkNode(n: root, min: Int.min, max: Int.max)
}
