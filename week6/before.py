# DYNAMIC PROGRAMMING
## Simple Array DP
### Length of Longest Subsequence
def longestSubsequenceLength(A):
    # Parameter: A is a list of integers
    # Output: Length of the longest subsequence that is first increasing then decreasing
    # Example: [1 11 2 10 4 5 2 1] -> [1 2 10 4 2 1] -> 6
    longest_sequence_length = 0
    list_length = len(A)
    B = list(A)
    B.reverse()

    li = [1] * list_length # longest increasing from 0 to index i
    ld = [1] * list_length # longest decreasing from index i to end
    ls = [1] * list_length # longestSubsequenceLength for the list up to this point

    for i in range(1, list_length):
        for j in range(i):
            if (A[i] > A[j]) and (li[i] < li[j] + 1):
                li[i] = li[j] + 1

    for x in range(1, list_length):
        for y in range(x):
            if (B[x] > B[y]) and (ld[x] < ld[y] + 1):
                ld[x] = ld[y] + 1

    for l in range(list_length):
        ls[l] = li[l] + ld[list_length - 1 - l] - 1

    longest_sequence_length = max(ls)
    return longest_sequence_length
