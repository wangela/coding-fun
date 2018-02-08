import Foundation

// TREES
class TreeNode {
    var val: Int = 0
    var left: TreeNode?
    var right: TreeNode?
}

// Inorder Traversal
func inorderTraversal(_ A: TreeNode?) -> [Int] {
    var traversal = [Int]()
    var tempStack = [TreeNode]()
    var curr_root = A
    
    while curr_root != nil || !tempStack.isEmpty {
        if curr_root != nil {
            tempStack.append(curr_root!)
            curr_root = curr_root!.left
        } else {
            curr_root = tempStack.popLast()
            traversal.append(curr_root!.val)
            curr_root = curr_root!.right
        }
    }
    return traversal
}

// Postorder Traversal
func postorderTraversal(_ A: TreeNode?) -> [Int] {
    if A == nil {
        return []
    }
    
    var traversal = [Int]()
    var tempStack = [TreeNode]()
    tempStack.append(A!)
    
    while !tempStack.isEmpty {
        let currNode = tempStack.popLast()
        if currNode!.left != nil {
            tempStack.append(currNode!.left!)
        }
        if currNode!.right != nil {
            tempStack.append(currNode!.right!)
        }
        traversal.append(currNode!.val)
    }
    
    return traversal.reversed()
}

// Preorder Traversal
func preorderTraversal(_ A: TreeNode?) -> [Int] {
    if A == nil {
        return []
    }
    var traversal = [Int]()
    var tempStack = [TreeNode]()
    tempStack.append(A!)
    
    while !tempStack.isEmpty {
        let currNode = tempStack.popLast()
        if currNode!.right != nil {
            tempStack.append(currNode!.right!)
        }
        if currNode!.left != nil {
            tempStack.append(currNode!.left!)
        }
        traversal.append(currNode!.val)
    }
    
    return traversal
}

// Level Order
// ZigZag Level Order BT
func zigzagLevelOrder(_ A: TreeNode?) -> [[Int]] {
    if A == nil {
        return [[]]
    }
    var traversal = [[Int]]()
    var ltor = true
    var levelStack = [TreeNode]()
    
    var currentLevel = [A!]
    var currentValues = [A!.val]
    ltor = false
    levelStack = currentLevel.reversed()
    currentLevel = []
    currentValues = []
    
    while !levelStack.isEmpty {
        let currNode = levelStack.popLast()
        currentValues.append(currNode!.val)
        if ltor {
            if currNode!.left != nil {
                currentLevel.append(currNode!.left!)
            }
            if currNode!.right != nil {
                currentLevel.append(currNode!.right!)
            }
        } else {
            if currNode!.right != nil {
                currentLevel.append(currNode!.right!)
            }
            if currNode!.left != nil {
                currentLevel.append(currNode!.left!)
            }
        }
        if levelStack.isEmpty {
            traversal.append(currentValues)
            ltor = !ltor
            levelStack = currentLevel.reversed()
            currentLevel = []
            currentValues = []
        }
    }
    
    return traversal
}

// BINARY SEARCH
// Search Answer
// Square Root of Integer
func sqrt(_ A: Int) -> Int {
    var left: Int = 0
    var right: Int = A
    
    while left <= right {
        let r = Int(floor(Double(left + right) / 2))
        let square = Int(pow(Double(r), 2))
        if square == A {
            return r
        } else if square < A {
            left = r + 1
        } else if square > A {
            right = r - 1
        }
    }
    left -= 1
    
    return left
}

// 
