# ARRAYS
##  Array Math

def maxSubArray(A):
    # Parameters:
    #   A is an array of integers (can be negative)
    # Return:
    #   An integer which is the sum of the contiguous subarray with the largest sum
    # Test cases:
    #   1. One element
    #   2. Only negative elements
    #   3. Normal multiple elements (positive and negative)
    #   4. Many elements

    maxSum = 0
    currSum = 0
    hasPositive = False
    maxNeg = A[0]

    for each in A:
        if each > 0:
            hasPositive = True
        currSum += each
        if currSum <= 0:
            currSum = 0
        maxSum = max(maxSum, currSum)
        maxNeg = max(each, maxNeg)

    if hasPositive == True:
        return maxSum
    else:
        return maxNeg

## Bucketing

def wave(A):
    # Parameters:
    #   A is a list of integers
    # Output:
    #   Return the array A sorted into a wave such that a1 >= a2 <= a3 >= a4 <= a5...
    #   If there are multiple possible arrays return the smallest lexigraphically

    B = sorted(A)
    C = []

    for index, each in enumerate(B):
        if index % 2 == 0:
            C.append(each)
        else:
            C.insert(index - 1, each)

    return C


# STRINGS
## Words

def reverseWords(A):
    # Parameters:
    #   A is a string
    # Output:
    #   Return the string in reverse order word by word
    #   A word is a sequence of non-space characters
    #   No leading or trailing spaces even if present in the input string
    #   Multiple spaces should be reduced to a single space
    #   Capitalization important?

    words = ""
    thisWord = ""
    currWord = []

    for letter in A:
        if letter.isspace():
            if len(currWord) > 0:
                if len(words) > 0:
                    currWord.append(" ")
                thisWord = ''.join(currWord)
                words = thisWord + words
            currWord = []
        else:
            currWord.append(letter)

    if (len(words) > 0 and len(currWord) > 0):
        currWord.append(" ")
    thisWord = ''.join(currWord)
    words = thisWord + words

    return words

##
