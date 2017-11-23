def longestConsecutive(A):
    # Argument:
    #   A is a list of unsorted integers
    # Output:
    #   Return an integer representing the length of the longest consecutive
    #   elements sequence. This should run in O(n) complexity.
    hash = set(A)
    longest = 0

    for ival in A:
        streak = 0
        # Is it the start of a sequence?
        if (ival - 1) not in hash:     # this is a start
            next = ival
            while(next in hash):        # if the next in the sequence is present
                streak += 1             # increment the streak
                next += 1
        longest = max(longest, streak)

    return longest
