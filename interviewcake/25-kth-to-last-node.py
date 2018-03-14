def kthToLastNode(A, k):
    # Parameter: A is the head node of a singly linked list and k is an integer
    # Output: The kth to last node of the list

    if A == None:
        return None

    current_node = A
    pointer_node = A

    for _ in range(k):
        if current_node == None:
            return "There are fewer than k nodes in this list"
        current_node = current_node.next

    while current_node != None:
        current_node = current_node.next
        pointer_node = pointer_node.next

    return pointer_node.data
