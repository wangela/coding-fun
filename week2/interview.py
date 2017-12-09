# Question 1
# Take an unsorted linked list and delete any duplicate values without using a temporary buffer or hash
# Example: 12 -> 11 -> 12 -> 21 -> 41 -> 43 -> 21 returns 12 -> 11 -> 21 -> 41 -> 43
# Also decide the time and space complexity

# Bonus
# Implement an alternative that uses a temporary storage buffer
# This should represent a significant improvement over the first solution in time complexity
# at the cost of space complexity

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

# Question 2
# IMplement a hashtable
# Can use arrays/lists
# Support generic value types
# Implement get, put, len, clear
# Support an initial default capacity of 16 entries
# get, put, remove, size, clear, and isEmpty
# Support an initial default capacity of 16 entries
# Support dynamic allocation of additional capacity as needed
#
# Hashtable: key = tuples, value = any type
# dictionary = { 'a': 1, 'b': 3}
# if 'a' in dictionary:
        # dict['a'] = 1
    # dict.getkeys()
#[ (), [] ]
#[ [('a'), [1]], [('b'), [3]] ]
# get('a') -> for each in dictionary: if each[0] == 'a' -> each[1]  else throw KeyError
def hash(immutable_object):
    result = math.pretend(immutable_object)
    return result

class HashTable(object):
    def __init__(self):
        self.arr = []

    def get(self, key):
        keyHash = math.hash(key)
        for each in self:
            if each[0] == keyHash:
                return each[1]
        throw error

    def put(self, key, value):
        if !isImmutable(key):
            throw error
        keyHash = math.hash(key)
        new = [keyHash, value]
        for index, each in enumerate(self.arr):
            if each == keyHash:
                self[index] = new
                return self
        self.arr.append(new)
        return self

    def remove(self, key):
        keyHash = math.hash(key)
        for index, each in enumerate(self.arr):
            if each == key:
                self.remove(key)
                return self

    def len(self):
        return len(self.arr)

    def clear(self):
        for each in self:
            self.arr.remove(each)
        return self

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
