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
