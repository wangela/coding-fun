# HASHING
## Key Formation
### Anagrams
def anagrams(A):
    # Parameters:
    #   A is an array of strings
    # Output:
    #   A list of all groups of strings that are anagrams.
    #   Represent a group as a list of integers representing the 1-based index
    #   of the string in the original array.
    # Example:
    #   ["cat", "dog", "god", "tca"] -> [[1,4], [2,3]]

    unique = {}
    result = []

    for index, each in enumerate(A):
        word = list(each)
        word.sort()
        dorw = tuple(word)
        if dorw in unique:
            unique[dorw].append(index + 1)
        else:
            unique[dorw] = [index + 1]

    for item in unique.keys():
        arr = unique[item]
        result.append(arr)

    return result


## Hash Search
### 2 Sum
def twoSum(A, B):
    # Parameters:
    #   A is a tuple of integers
    #   B is an integer
    # Output:
    #   Return a list of integers
    #   The list should have the indices of two numbers from A that add up to B
    #   Index 1 < Index 2
    #   Indices are 1-based not 0-based
    #   If multiple solutions exist, return the one where index 2 is minimum
    #   If multiple soulutions exist using index 2, choose where index 1 is minimum
    # Example:
    #   [2, 7, 11, 15] target = 9 --> [1, 2]

    # Test Cases:
    #   (0, 0) target = 0 --> [1, 2]
    #   (0, 1) target = 1 --> [1, 2]
    #   (1, 0) target = 1 --> [1, 2]
    #   (1, 1, 1, 1, 1) target = 2 --> [1, 2]
    #   (-2, 1, 11, 2, 7, 15) target = 9 --> [1,3]
    )

    # Approach:
    #   Convert the tuple to a dictionary with the integers as keys and the indices as values
    #   Test combos of keys to see which add up to the target
    #   Pick the lowest indices among the values for those keys
    #   Order the indices in the right order

    unique = {}
    result = []
    pairs = []

    for index, each in enumerate(A):
        if each in unique:
            unique[each].append(index + 1)
        else:
            unique[each] = [index + 1]

    for item in unique.keys():
        c = B - item
        pair = []
        if c in unique:
            pair.append(unique[c][0])
            if c == item:
                if len(unique[c]) > 1:
                    pair.append(unique[c][1])
                else:
                    continue
            else:
                pair.append(unique[item][0])
            pair.sort()
            pairs.append(pair)

    pairs.sort(key=lambda x: x[0])
    pairs.sort(key=lambda x: x[1])

    if len(pairs) > 0:
        return pairs[0]
    else:
        return pairs


# LINKED LISTS
## List 2 pointer
### Palindrome List
# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def convertToLinkedList(A):
    x = ListNode(A[0])
    head = x

    for each in A[1:]:
        y = ListNode(each)
        x.next = y
        x = y

    return head

def lPalin(A):
    # Parameters:
    #   A is the head node of a singly linked list
    # Output:
    #   Return 1 if it is a palindrome
    #   Return 0 if it is not a palindrome
    # Goal:
    #   Linear O(n) time and Constant O(1) space
    # Example:
    #   List 1 --> 2 --> 1 --> null is a palindrome. Return 1
    #   List 1 --> 2 --> 3 --> null is not a palindrome. Return 0
    # Inefficient Approach:
    #   As we walk through; make an array copy
    #   Make pointers to the beginning and ends of the array and walk toward the middle
    #   If elements at pointers match until the middle, return 1
    #   If any elements do not match on the way, return 0
    #   O(n) time but also O(n) space
    # Efficient Approach:
    #   As we walk through; make a prev property to convert it to a doubly linked list
    #   Walk through again from both ends and compare
    #   O(n) time and O(1) space
    first = ListNode(A.val)
    this = first
    current = A
    prev = None

    while current.next != None:
        second = ListNode(current.next.val)
        next = current.next
        first.next = second
        current.next = prev
        prev = current
        current = next
        first = second
    current.next = prev
    reverse = current
    forward = this

    while forward != None and reverse != None:
        if forward.val != reverse.val:
            return 0
        else:
            forward = forward.next
            reverse = reverse.next

    return 1


## List Math
### Add Two Numbers As Lists
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def addTwoNumbers(A, B):
    currA = A
    currB = B
    carry = [0]
    answer = None
    sumList = None

    while currA != None or currB != None:
        currC = 0
        if int(carry[0]) > 0:
            currC = int(carry[-1])
            carry = carry[:-1]
            if len(carry) == 0:
                carry = [0]
        if currA == None:
            sum = currB.val + currC
        elif currB == None:
            sum = currA.val + currC
        else:
            sum = currA.val + currB.val + currC
        if sum > 9:
            sumStr = str(sum)
            sumLetters = list(sumStr)
            if sumList != None:
                next = ListNode(int(sumLetters[-1]))
                sumList.next = next
                sumList = next
            else:
                answer = ListNode(int(sumLetters[-1]))
                sumList = answer
            carry = sumLetters[:-1]
        else:
            if sumList != None:
                next = ListNode(sum)
                sumList.next = next
                sumList = next
            else:
                answer = ListNode(sum)
                sumList = answer
        if currA == None:
            currB = currB.next
        elif currB == None:
            currA = currA.next
        else:
            currA = currA.next
            currB = currB.next

    if int(carry[0]) > 0:
        for digit in carry:
            sumList.next = ListNode(int(digit))
            sumList = sumList.next
    sumList.next = None

    return answer
    # Parameters:
    #   A is the head node of a linked list representing a non-negative number
    #   B is the head node of a linked list representing a non-negative number
    #   Digits are stored in reverse order (smallest to largest magnitude),
    #   each node containing a single digit
    # Output:
    #   Return the head node in the linked list representing the sum of the two numbers
    #   Ensure there are no trailing zeros in the result
    # Example:
    #   (2 -> 4 -> 3) + (5 -> 6 -> 4) = 342 + 564 = 807 = (7 -> 0 -> 8)
    # Test Cases:
    #   A or B is 0
    #   A = 0 and B = 0
    #   Cause a trailing zero and remove it
    #   Can input have trailing zeros?
