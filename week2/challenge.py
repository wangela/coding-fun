# CHALLENGE 1
# Implement LinkedListNode class
# Each instance represents a single node in the list
class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next
        return self

# Also implement a convenience method to initialize a whole list from an array of values
def set_values_from_array(listValues):
    current = LinkedListNode(listValues[0])
    head = current
    for each in listValues[1:]:
        new = LinkedListNode(each)
        current.setNext(new)
        current = new

    return head

# CHALLENGE 3
# Time and Space Complexity of set_values_from_array method
# O(n) for each in listValues
# O(1) for the method because it only uses space current, head, and new variables (constant)

# Time and Space Complexity of Add Two Numbers problem in Challenge #2
# O(a + b) time
# O(1) space

# CHALLENGE 6
# Longest Non-Repeating Substring
def longest_substring(A):
    # Parameters: A is a string
    # Output: Integer, length of the longest non-repeating substring
    # Example: "abcabcbb" --> substring is "abc" --> return 3
    #   "aaaaaaaa" --> substring is "a" --> return 1
    seen = set()
    maxLength = 0
    count = 0

    for idx, letter in enumerate(A):
        count = 0
        for char in A[idx:]:
            if char in seen:
                maxLength = max(maxLength, count)
                seen = set()
                break
            else:
                seen.add(char)
                count += 1
                continue
        maxLength = max(maxLength, count)

    return maxLength
