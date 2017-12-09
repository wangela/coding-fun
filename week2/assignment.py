# HASHING
##
###
def fname(arg):
    pass


## Hashing two pointer
### Window string
def minWindow(A, B):
    # Parameters:
    #   A is a string
    #   B is a string
    # Output:
    #   String that is the minimum window in A that contains all the letters of B
    #   If character C is repeated n times in B, C should appear a minimum of n times
    #   in the minimum window of A as well.
    #   If no such window exists, return empty string.
    #   If there are multiple windows, return the first occurring window
    # Complexity Goal:
    #   O(n) time
    # Example:
    #   'ADOBECODEBANC', 'ABC' -> 'BANC'
    # Approach:
    #   start and end pointers for the window
    #   hash for the characters in B (dictionary to count repeated)
    #   check if characters are in dictB and decrement if so
    #   extend the end until dictB is empty 0...5
    #   mark length
    #   shrink the start to see if there's a shorter window 3...5
    #   extend the end until dictB is empty 3...10
    #   compare length to min_length
    #   shrink the start to see if there's a shorter window 5...10
    #   shrink the start to see if there's a shorter window 9..10
    #   extend the end until dictB is empty 9...12
    #   compare length to min_length
    import copy

    curr_start = 0
    curr_end = len(B) - 1
    curr_length = 0
    min_length = len(A) + 1
    min_start = curr_start
    min_end = curr_end

    dictb = {}

    for character in B:
        if character in dictb:
            dictb[character] += 1
        else:
            dictb[character] = 1
    if len(dictb) == 0:
        return ""
    backup_dictb = copy.deepcopy(dictb)

    for j in range(len(A)):
        curr_start = j
        curr_length = 0
        dictb = copy.deepcopy(backup_dictb)
        for i in range(j, len(A)):
            curr_end = i
            key = A[i]
            if key in dictb:
                value = dictb[key]
                if value > 1:
                    dictb[key] -= 1
                elif value == 1:
                    del dictb[key]
                    if len(dictb) == 0:
                        curr_length += 1
                        if curr_length < min_length:
                            min_start = curr_start
                            min_end = curr_end
                        min_length = min(curr_length, min_length)
                        break
            curr_length += 1

    if min_length > len(A):
        return ""
    else:
        sub = A[min_start:min_end + 1]
        return sub


# LINKED LISTS
## List sort
### Insertion Sort List
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def convert(list_representation):
    d = [int(x) for x in list_representation.split(" -> ")]
    a = set_values_from_array(d)
    return a

def set_values_from_array(listValues):
    current = ListNode(listValues[0])
    head = current
    for each in listValues[1:]:
        new = ListNode(each)
        current.next = new
        current = new

    return head

def insertionSortList(A):
    # Parameters: A the head node of an unsorted linked list
    # Perform: Use insertion sort to sort the list
    # Output: The head node of the sorted list
    # Example: 1 -> 3 -> 2 returns 1 -> 2 -> 3
    # Questions: Any duplicates? Minimum length of list?
    # Approach:
    #   Start with second element
    #   Isolate it and point prev.next to curr.next
    #   Compare to head
    #   If < head, insert to head. If > head, insert after head.
        # Set curr.next to head
        # Set head.next to head.next.next
    #   Keep looking left until > left or until reach last_sorted
    # 5 -> 66 ->68 -> 42->  73-> 3-> 5 -> 8 -> 9 -> None
    # LS    C
    #       L           R
    if A.next == None:
        return A

    head = A            #1
    left = A
    last_sorted = A
    curr = last_sorted.next       #2
    right = curr.next   #3

    if curr.val < left.val:
        temp = curr.next
        curr.next = left
        left.next = temp
        head = curr
        last_sorted = left
        curr = last_sorted.next
    else:
        last_sorted = curr
        curr = curr.next

    while (curr != None):
        # Skip curr and isolate it for now
        last_sorted.next = curr.next # 9 -> None

        # start from the head
        left = head               #1
        left_value = left.val   #1
        right = left.next       #2
        right_value = right.val #2
        curr_value = curr.val   #3
        #print("currently", curr_value)
        while (right != None and left != last_sorted and last_sorted != None and curr != None):
            #print("curr" , curr_value, "left", left_value, "right", right_value, "leftPointer", last_sorted.val)
            # sort curr against the left window
            if curr_value < left_value:
                temp = curr.next
                curr.next = left
                if left == head:    # if we are at the head, reset head to curr
                    head = curr
                curr = temp
                # last_sorted stays where it is
                break
            # sort curr between left and right window
            elif curr_value < right_value:
                temp = curr.next    # None
                left.next = curr    # 3 -> 3
                curr.next = right   #  3 -> 5 (head is still #1)
                curr = temp         # None
                # last_sorted stays where it is
                break
            # curr is greater than right; keep moving window right
            # until left = last_sorted
            # once left = last_sorted, curr is the new greatest and
            # last_sorted can skip to the next
            else:
                temp = right.next       #
                left = right            # 5
                left_value = left.val   # 5
                right = temp            # 9
                if right == None:
                    break
                right_value = right.val # 9
        if left == last_sorted:
            last_sorted.next = curr # Restore connection to current in list
            last_sorted = curr         # 9
            curr = curr.next            #8

    return head


## Pointer Move
### Swap List Nodes in Pairs
def swapPairs(A):
    # Parameters: A is the head node of a linked list
    # Perform: Swap every two adjacent nodes in the list
    # Output: The head node of the linked list
    # Goal: O(1) extra space, do not modify the values of the nodes
    # Example:
    #   1 -> 2 -> 3 -> 4 returns 2 -> 1 -> 4 -> 3
    #   1 -> None returns 1 -> None
    #   1 -> 3 -> 2 returns 3 -> 1 -> 2
    # Questions:
    #   Minimum length of list? What to return if odd number of nodes?
    # Approach:
    #   Set first node.next to .next.next
    #   Set second node.next to first
    #   Advance the pointers so first = first.next and second = first.next.next
    #   Stop when .next is None or .next.next is None
    # 28 -> 34 -> 48 -> 74 -> 42

    if A.next == None:
        return A
    first = A    #28
    second = first.next #34
    head = second       #34 -> 28 -> 74 -> 48 -> 42

    while (first != None and second != None):
        # swap the pair
        first.next = second.next    #48 -> 42
        second.next = first         #74 -> 48

        # advance the pointers
        old_first = first           #48
        first = first.next          #42
        if first == None:   # even number of nodes, end reached
            return head
            break
        second = first.next         #None
        if second != None:
            old_first.next = second     #48 -> None

    # odd number of nodes, end reached
    return head
