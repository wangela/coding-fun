class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildList():
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    A.next = B
    B.next = C
    C.next = D
    D.next = E

    return A

def subtract(A):
    # Arguments:
    #   A is the head node of a singly linked list
    # Output:
    #   Return the head node of a list where the floor (length/2) nodes
    #   are modified such that
    #   First node = last node - first node
    #   Second node = second-to-last node - second node
    # Goal:
    #   Implement with constant extra space

    length = 0
    node = A
    while (node != None):
        length += 1
        node = node.next
    if length % 2 == 1:
        odd = True
    else:
        odd = False
    if length == 1:
        return A

    length = length // 2     # Identify half the length of the list using floor division

    current = A
    prev = None
    index = 0
    while (index < (length - 1)): # Traverse and reverse until the halfway mark
        next = current.next
        current.next = prev
        prev = current
        current = next
        index += 1

    if odd:
        fnext = current.next.next
    else:
        fnext = current.next
    midpoint = True
    while (index >= 0):   # Traverse backwards and re-reverse until the beginning
        current.val = fnext.val - current.val
        if midpoint:
            next = prev
            midpoint = False
        else:
            next = current.next
            current.next = prev
        prev = current
        current = next
        fnext = fnext.next
        index -= 1

    node = prev                 # Prev is the head node since current ends as null
    return node

def subtractWithPrint(A):
    # Arguments:
    #   A is the head node of a singly linked list
    # Output:
    #   Return the head node of a list where the floor (length/2) nodes
    #   are modified such that
    #   First node = last node - first node
    #   Second node = second-to-last node - second node
    # Goal:
    #   Implement with constant extra space

    length = 0
    node = A
    while (node != None):
        length += 1
        node = node.next
    if length % 2 == 1:
        odd = True
    else:
        odd = False
    print("odd =", odd)
    print("length =", length)
    if length == 1:
        return A
    length = length // 2     # Identify half the length of the list using floor division
    print("halfway = ", length)

    current = A
    prev = None
    index = 0
    while (index < (length - 1)): # Traverse and reverse until the halfway mark
        next = current.next
        current.next = prev
        prev = current
        current = next
        index += 1

    print("traversed until index", index)
    if odd:
        fnext = current.next.next
    else:
        fnext = current.next
    midpoint = True
    while (index >= 0):   # Traverse backwards and re-reverse until the beginning
        print("current.val =", current.val, "fnext.val =", fnext.val)
        current.val = fnext.val - current.val
        if midpoint:
            next = prev
            midpoint = False
        else:
            next = current.next
            current.next = prev
        prev = current
        current = next
        fnext = fnext.next
        index -= 1
        print("index =", index)

    node = prev                 # Prev is the head node since current ends as null
    while (node != None):
       print(node.val)
       node = node.next
    return prev
