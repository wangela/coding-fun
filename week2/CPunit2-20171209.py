# Python 3 version
def degrees_to_anagram2():
    # Parameters:
    #   C is a string resulting from concatentation of two strings, A and B.
    #   A is a string of length n
    #   B is a string of length m
    #   |n - m| <= 1
    #   all lowercase, no spaces in the strings
    # Output:
    #   Return the minimum number of characters in A that need to change
    #   to make A an anagram of B.
    #   No addition or deletion of characters from A, only replacement.
    #   Return -1 if not possible
    # Examples:
    #   'aaa','bbb'-> 3
    #   'a','b' -> 1
    #   'ab','c' -> -1
    #   'mn', 'op' -> 2
    #   'xy', 'yx' -> 0
    n = int(input())
    for i in range(n):
        degrees = -1
        C = str(input())
        if len(C) % 2 == 1:
            print(degrees)
            continue
        else:
            individual_lengths = len(C)//2
            degrees = 0

        A = C[0:individual_lengths]
        B = C[individual_lengths:len(C)]
        dict_b = {}

        for character in B:
            if character in dict_b:
                dict_b[character] += 1
            else:
                dict_b[character] = 1

        for character in A:
            if character in dict_b:
                value = dict_b[character]
                if value > 1:
                    dict_b[character] -= 1
                elif value == 1:
                    dict_b.pop(character, None)
            else:
                degrees += 1

        print(degrees)

# Python 2 version
def degrees_to_anagram2():
    # Parameters:
    #   C is a string resulting from concatentation of two strings, A and B.
    #   A is a string of length n
    #   B is a string of length m
    #   |n - m| <= 1
    #   all lowercase, no spaces in the strings
    # Output:
    #   Return the minimum number of characters in A that need to change
    #   to make A an anagram of B.
    #   No addition or deletion of characters from A, only replacement.
    #   Return -1 if not possible
    # Examples:
    #   'aaa','bbb'-> 3
    #   'a','b' -> 1
    #   'ab','c' -> -1
    #   'mn', 'op' -> 2
    #   'xy', 'yx' -> 0
    n = int(raw_input())
    for i in range(n):
        degrees = -1
        C = str(raw_input())
        if len(C) % 2 == 1:
            print degrees
            continue
        else:
            individual_lengths = len(C)//2
            degrees = 0

        A = C[0:individual_lengths]
        B = C[individual_lengths:len(C)]
        dict_b = {}

        for character in B:
            if character in dict_b:
                dict_b[character] += 1
            else:
                dict_b[character] = 1

        for character in A:
            if character in dict_b:
                value = dict_b[character]
                if value > 1:
                    dict_b[character] -= 1
                elif value == 1:
                    dict_b.pop(character, None)
            else:
                degrees += 1

        print degrees

# Python 2
def sum():
    n = int(raw_input())
    for i in range(0,n):
        a, b = raw_input().split()
        print int(a) + int(b)

# Python 3
def sum3():
    n = int(input())
    for i in range(n):
        a, b = input().strip().split(' ')
        print (int(a) + int(b))

3
1 5
6 10
999 -33445

5
aaabbb
ab
abc
mnop
xyyx

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail

# Python3 version
def removeNodes(list, x):
    # Parameters:
    #   list is the head of a linked list
    #   x is an integer
    # Perform:
    #   Remove all nodes with value > x
    # Output:
    #   Return the head of the modified linked list
    # Example:
    #   1 -> 2 -> 3 -> 4 -> 5 -> None, 3 returns 1 -> 2 -> 3 -> None
    #   5 -> 2 -> 1 -> 6 -> 7 -> None, 5 returns 5 -> 2 -> 1 -> None
    head = list     #1
    cursor = head   #1
    prev = head     #1

    while (cursor != None):
        value = cursor.val  #5
        next = cursor.next  #None
        if value > x:
            if cursor == head:
                head = next
                cursor = next
                prev = head
            else:
                prev.next = next    #3 -> None
                # prev stays the same
                cursor = next       #None
        else:
            prev = cursor   #
            cursor = next   #

    return head

# Python 3
def firstRepeatedWord(s):
    # Parameter: s is a string describing a sentence
    #   0 < |s| < 1024
    #   delimiters: space, tab, ',', ':', ';', '-', '.'
    #   s contains >= 1 repeated words
    #   each word is separated by one or more delimiters
    # Perform:
    #   Word is a sequence of letters(a-z and A-Z) delimited by space or non-letter
    #   Detect a repeated word.
    #   Case sensitive (had =/= Had)
    #   Substrings are not considered repeating
    # Output: Return a string containing the first repeated word in the sentence
    # Examples:
    #   He had had quite enough of this nonsense. -> had
    l = s
    for character in ',:;-.':
        l = l.replace(character, ' ')

    words = l.split()
    glossary = set()

    for word in words:
        if word in glossary:
            return word
        else:
            glossary.add(word)

    return "No repeated word found"
