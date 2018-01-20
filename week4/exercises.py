# RECURSION / BACKTRACKING
## Subsets
### Combinations
def combine(A, B):
    # Parameters: A and B are integers
    # Perform: Return all possible combinations of B numbers out of 1 2 3...A.
    #   Make sure the elements in each combination are sorted and the combinations are sorted.
    # Output: An array of sorted combinations (in list form)
    # Clarification: A, B always positive?

    return combine_util(1, A+1, B)

def combine_util(start, end, B):
    # Parameters: start, end, and B are integers
    # Output: A list of every combination in A with B elements
    if end - start == B:
        return [list(range(start, start + B))]
    elif B == 0:
        return [[]]

    answer = []

    for i in range(start, end + 1 - B):
        for combo in combine_util(i + 1, end, B- 1):
            answer.append([i] + combo)

    return answer

def combine_util_alt(A, B):
    # Parameters: A is a list, B is an integer
    # Output: A list of every combination in A with B elements
    answer = []
    for i in range(len(A)):
        if B == 1:
            answer.append(A[i])
        else:
            for c in combine_util(A[i + 1:], B - 1):
                combo.append(A[i])
                combo.append(c)
                answer.append(combo)
    return answer

# BIT MANIPULATION
## Bit Play
### Number of 1 Bits
def numSetBits(A):
    # Parameter: A is an unsigned integer in binary representation
    # Output: Return an integer of the number of "1" bits in A
    # Example: 32-bit integer 11 has binary representation 00000000000000000000000000001011
    #   Return 3
    #  110110
    #  110101
    #  110100 +1
    #  110011
    #  110000 +2
    #  101111
    #  100000 +3
    #  011111
    #  000000 +4
    count = 0
    while(A):
        A &= A - 1
        count += 1
    return count

## Bit Manipulation
### Single Number
def singleNumber(A):
    # Input: A is a list of integers, where every element appears twice except for one. Find that single one
    # Perform: Linear time complexity, no extra memory
    # Output: The single integer that is not repeated in the list
    value = 0
    for i in range(0, len(A)):
        value ^= A[i]
    return value

## Bucketing
### Min XOR Value
def findMinXor(A):
    # Input: A is a list of integers (2 <= N <= 100,000) (0 <= A[i]<= 1,000,000,000)
    # Perform: Find the pair of integers with the smallest XOR value
    # Output: The minimum XOR value
    # Examples:
    #   Input [0, 2, 5, 7]
    #   Outuput 2 (0 ^ 2)
    #   Input [0, 4, 7, 9]
    #   Output 3 (4 ^ 7)
    A.sort()
    length = len(A)
    last = length - 1
    min_xor = A[last] ^ A[last - 1]
    print(min_xor)
    latest = A[last - 1]
    for i in range(last - 2, -1, -1):
        if A[i] > min_xor:
            latest = A[i]
            continue
        else:
            curr_xor = latest ^ A[i]
            if curr_xor < min_xor:
                min_xor = curr_xor
                print(min_xor)
            latest = A[i]
    return min_xor

def findMinXor_naive(A):
    # Input: A is a list of integers (2 <= N <= 100,000) (0 <= A[i]<= 1,000,000,000)
    # Perform: Find the pair of integers with the smallest XOR value
    # Output: The minimum XOR value
    # Examples:
    #   Input [0, 2, 5, 7]
    #   Outuput 2 (0 ^ 2)
    #   Input [0, 4, 7, 9]
    #   Output 3 (4 ^ 7)
    min_xor = max(A)
    length = len(A)
    for i in range(0, length):
        for j in range(i+1, length):
            curr_xor = A[i] ^ A[j]
            if curr_xor < min_xor:
                min_xor = curr_xor
    return min_xor

### Mock Interview
# A xor B
#   110110
#   011001
#   101111
#   0101
#   1001
#   1100 --> 12
#   1111 --> 15
#   1001 --> 9
#   1000
#   0110 --> 6
#   0101 --> 5
#   0011
#   0110 --> 15 xor 9 is 6
#   1111 --> 6 xor 9 is 15
#   U >> 1
#   1110 --> 14
#   1010 --> 10
#   0010 --> 2
def max_xor(lower, upper):
    msb = get_msb(upper)
    lsbm = get_ls1(upper)
    lsbl = get_ls1(lower)
    lsb = lsbm
    if lsbl < lsb:
        lsb = lsbl
    target = max_bits(msb, lsb)
    return target

def get_msb(value):
    count = 0
    while value:
        value = value >> 1
        count += 1
    return count

def get_ls1(value):
    count = get_msb(value ^ (value - 1))
    return count

def max_bits(most, least):
    all_ones = 0
    power = 0
    for i in range(1, least):
        power += 1
    for j in range(least, most + 1):
        all_ones += 2**power
        power += 1
    return all_ones

### Challenge 1
def factorial(N):
    if N == 1:
        return 1
    else:
        return N * factorial(N - 1)

### Challenge 2
def gcd(A, B):
    greater = B
    lesser = A
    if A > B:
        greater = A
        lesser = B
    if lesser == 0:
        return greater
    else:
        return gcd(greater % lesser, lesser)

### Challenge 3
def permute(A):
    # Input: A is a list of 2 or more integers
    # Output: ALl permutations of the list. Assume all numbers are unique
    length = len(A)
    permutations = permute_util(A, 0, length)

def permute_util(A, start, end):
    permutations = []
    if end - start = 1:
        perm1 = []
        perm1.append(A[start])
        perm1.append(A[end])
        perm2 = []
        perm2.append(A[end])
        perm2.append(A[start])
        permutations.append(perm1)
        permutations.append(perm2)
        return permutations
    else:
        for each in A:
            permutations.append(each)
            for permutation in permute_util(A)
