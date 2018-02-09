import Foundation

class LinkedListNode<Value: Equatable> {
    
    var value: Value
    var next: LinkedListNode?
    
    init(_ value: Value) {
        self.value = value
    }
}

enum DeleteNodeError: Error, CustomStringConvertible {
    case lastNode
    
    var description: String {
        return "Can't delete the last node with this technique!"
    }
}


func deleteNode(_ target: LinkedListNode<T: Equatable>?) -> LinkedListNode<T>? {
    if let target = target {
        var nextNode = target.next
        if nextNode != nil {
            var skipNext = nextNode!.next
            target.value = nextNode!.value
            target.next = skipNext
            return target
        } else {
            return nil
        }
    } else {
        throw DeleteNodeError.lastNode
    }
}

let a = LinkedListNode("A")
let b = LinkedListNode("B")
let c = LinkedListNode("C")

a.next = b
b.next = c
a
b
try deleteNode(b)

b
