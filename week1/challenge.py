# Challenge 1
# ARRAYS
## Delete Duplicates From Sorted Array
def remove_duplicates(A):
    # Parameters: A is a sorted array of integers
    # Perform: Remove all duplicates,
    #   shift valid elements left to fill emptied indices,
    #   all remaining indices are set to 0.
    # Output: Integer, the number of remaining valid elements
    # Complexity Goal: O(n) time and O(1) additional space
    # Example:
    #   {2,3,5,5,7,11,11,11,11,13} --> {2,3,5,7,11,13,0,0,0} --> 0

    next_unique = 0
    duplicate = -1

    for index, each in enumerate(A):
        if index == 0:
            continue
        if each == A[index - 1]:
            duplicate = each
        else:
            next_unique += 1
            A[next_unique] = each

    if next_unique next_unique += 1
    for item in A[next_unique:]:
        item = 0

    return duplicate

### InterviewBit version: Find Duplicate in Array
def repeatedNumber(A):
    # Parameters: A is a tuple of n+1 integers between 1 and n
    # Perform: Find one number that repeats itself
    # Output: Integer (the number that repeats itself).
    #   If there are multiple duplicates, just choose any one to return.
    #   If there are no duplicates, return -1
    # Complexity Goal: O(n) time and less than O(n) additional space, traverse
    #   the stream sequentially only O(1) times
    # Example:
    #   [3 4 1 4 1] --> 1
    #   [1 1 1 1] --> 1
    #   [1 2 3] --> -1
    # Approach:
    #   Make a parallel hash set and compare the current element to the hash

    duplicate = -1
    parallel = set()

    for each in A:
        if each in parallel:
            return each
        else:
            parallel.add(each)

    return duplicate


# Challenge 4
## STRINGS
### Palindrome Detection
### InterviewBit version: Palindrome String
def isPalindrome(A):
    # Parameters: A is a string
    # Output: Return an integer: 0 if not a palindrome, 1 if is a Palindrome
    #   Consider only alphanumeric characters
    #   Ignore case

    B = ""
    for char in A:
        if char.isalnum():
            B += char.casefold()
    if len(B) <= 1:
        return 1
    tail = len(B) - 1

    for head in range(math.floor(len(B)/2)+1):
        if B[head] != B[tail]:
            return 0
        else:
            tail -= 1
            continue

    return 1
