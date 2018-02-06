// LINKED LISTS
// List 2 Pointer
// Remove Duplicates from Sorted List
import Foundation

class ListNode {
    var val: Int = 0
    var next: ListNode?
}

func deleteDuplicates(_ A: ListNode?) -> ListNode? {
    // Parameter: A is the head node of a sorted linked list
    // Output: Return the head node of the linked list with all duplicates deleted such that each element appears only once
    let head = A
    var current = head
    
    while current != nil {
        while current?.next != nil && current?.next?.val == current?.val {
            current?.next = current?.next?.next
        }
        current = current?.next
    }
    
    return head
}

func removeNthFromEnd(_ A: ListNode?, _ B: inout Int) -> ListNode? {
    var head = A
    var beforeB: ListNode? = nil
    var nodeB: ListNode? = head
    var forward: ListNode? = head
    
    if head == nil { return head }
    
    for _ in 1...B {
        if forward?.next == nil {
            head = head?.next
            return head
        }
        forward = forward?.next
    }
    
    while forward != nil {
        beforeB = nodeB
        nodeB = nodeB?.next
        forward = forward?.next
    }
    
    beforeB?.next = nodeB?.next
    
    return head
}

func isValidSudoku(_ board: [[Character]]) -> Bool {
    // Check all rows
    for r in 0..<9 {
        var rowCheck = Set<Character>()
        for x in 0..<9 {
            let digit = board[r][x]
            if digit == "." {
                continue
            } else if rowCheck.contains(digit) {
                return false
            } else {
                rowCheck.insert(digit)
            }
        }
    }
    
    // Check all columns
    for c in 0..<9 {
        var colCheck = Set<Character>()
        for y in 0..<9 {
            let digit = board[y][c]
            if digit == "." {
                continue
            } else if colCheck.contains(digit) {
                return false
            } else {
                colCheck.insert(digit)
            }
        }
    }

    // Check all boxes
    for b in 0..<3 {
        for x in 0..<3 {
            var boxCheck = Set<Character>()
            for y in 0..<3 {
                for z in 0..<3 {
                    let digit = board[(3 * x) + y][(3 * b) + z]
                    if digit == "." {
                        continue
                    } else if boxCheck.contains(digit) {
                        return false
                    } else {
                        boxCheck.insert(digit)
                    }
                }
            }
        }
    }
    
    return true
}

//let sample = [["5", "3", ".", ".", "7", ".", ".", ".", "."], [6, ".", ".", 1, 9, 5, ".", ".", "."], [".", 9, 8, ".", ".", ".", ".", 6, "."], [8, ".", ".", ".", 6, ".", ".", ".", 3], [4, ".", ".", "8", ".", 3, ".", ".", 1], [7, ".", ".", ".", 2, ".", ".", ".", 6], [".", 6, ".", ".", ".", ".", 2, 8, "."], [".", ".", ".", 4, 1, 9, ".", ".", 5], [".", ".", ".", ".", 8, ".", ".", 7, 9]]
//isValidSudoku(sample)

func diffPossible(_ A: [Int], _ B: Int) -> Int {
    var complements: Set = Set<Int>()
    
    for first in A {
        let plus = first + B
        let minus = first - B
        if complements.contains(plus) || complements.contains(minus) {
            return 1
        }
        complements.insert(first)
    }
    return 0
}


