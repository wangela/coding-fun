# GUIDE
# Search for string "\n## " to count number of/jump to category buckets completed
# Search for string "### " to count number of/jump to individual questions completed

# ARRAYS
## Simulation array
### Pascal Triangle
def generate(A):
    # Parameters:
    #   A is an integer representing the number of rows of Pascal's triangle to generate
    # Output:
    #   An array of Pascal's triangle to A rows,
    #   such that A[C] in row R = A'[C] + A'[C-1] in row R-1
    #   and the first and last elements of each row are 1

    # Example:
    # Input: 5
    # Output:
    # [
    #   [1],    0 = 1
    #   [1,1],  1 = 1, 1
    #   [1,2,1] 2 = 1, 2, 1
    #   [1,3,3,1]   3 = 1, 3, 3, 1
    #   [1,4,6,4,1] 4 = 1, 4, 6, 4, 1

    out = []

    for i in range(A):
        row = []
        row.append(1)
        for each in range(1, i):
            prev = out[i - 1]
            row.append(prev[each] + prev[each - 1])
        if i > 0:
            row.append(1)
        out.append(row)

    return out

### Kth Row of Pascal's Triangle
def getRow(A):
    # Parameters:
    #   A is an integer. It is zero-based, so 0 is equivalent to the first row [1]
    # Output:
    #   An array equivalent to the Ath row of Pascal's triangle,
    #   such that A[C] in row R = A'[C] + A'[C-1] in row R-1
    #   and the first and last elements of each row are 1
    # Goal:
    #   Optimize to use O(A) extra space

    # Example:
    # Input: 3
    # Output:
    #   [1, 3, 3, 1]

    prev = [1]
    row = []

    if A == 0:
        return prev

    for i in range(1, A + 1):
        row = []
        row.append(1)
        for each in range(1, i):
            row.append(prev[each] + prev[each - 1])
        row.append(1)
        prev = row

    return row


## Value Ranges
### Merge Intervals
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(interval1, interval2):
    if interval2 == None:
        result = 0, interval1
        return result

    minmin = min(interval1.start, interval2.start)
    maxmax = max(interval1.end, interval2.end)

    if minmin == interval1.start and interval2.start > interval1.end:
        result = 0, interval1, interval2
        return result
    elif minmin == interval2.start and interval1.start > interval2.end:
        result = 1, interval2, interval1
        return result
    else:
        result = 2, Interval(minmin, maxmax)
        return result

def insert(intervals, new_interval):
    # Parameters:
    #   A set? list? of non-overlapping intervals and one new interval.
    #   The intervals are sorted according to their start times.
    # Output:
    #   Insert the new interval into the other intervals. Merge if necessary.
    #   Returned intervals should also be sorted

    # Example:
    # Input:
    #   [1,3], [6,9] and new interval [2,5]
    # Output:
    #   [1,5], [6,9] (2 fell inside the [1,3] interval so they were merged)

    # Example:
    # Input:
    #   [1,2],[3,5],[6,7],[8,10],[12,16] and new interval [4,9]
    # Output:
    #   [1,2],[3,10],[12,16] (4 fell inside[3,5] and 9 fell inside [8,10]
    #   and [6,7] is contained within [4,9] so all four were merged into [3,10])

    # Test cases:
    #   Empty set for input returns new interval as is
    #   Empty new interval returns original set as is
    #   New interval is completely before original intervals
    #   New interval is completely after original intervals
    #   New interval is inside with various merge intersections
    #   New interval completely encompasses all original intervals

    # Approach:
    #   Check for placement of new interval min
    #   Check for placement of new interval max
    #   If needed, check and perform merges
    if intervals == []:
        return [new_interval]
    elif new_interval == None:
        return intervals

    if new_interval.start > new_interval.end:
        new_interval = Interval(new_interval.end, new_interval.start)
        print new_interval.start
        print new_interval.end

    new_min = new_interval.start
    new_max = new_interval.end
    num_intervals = len(intervals)
    orig_min = intervals[0].start
    orig_max = intervals[num_intervals - 1].end

    if new_min > orig_max:
        intervals.append(new_interval)
        return intervals
    elif new_min < orig_min:
        if new_max < orig_min:
            intervals.insert(0, new_interval)
            return intervals
        elif new_max > orig_max:
            return [new_interval]

    result = []
    for each in intervals:
        try_merge = merge(each, new_interval)
        if try_merge[0] == 0:      # Unchanged: not overlapping and in correct order
            result.append(each)
            continue
        elif try_merge[0] == 1:    # new_interval is less and not overlapping
            result.append(new_interval)
            result.append(each)
            new_interval = None
            continue
        elif try_merge[0] == 2:    # new_interval is overlapping and merged
            new_interval = try_merge[1]
    if new_interval:
        result.append(new_interval)

    return result


### Merge Overlapping Intervals
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
def mergetwo(interval1, interval2):
    answer = []

    minmin = min(interval1.start, interval2.start)
    maxmax = max(interval1.end, interval2.end)

    if minmin == interval1.start:           # interval1 has earlier start
        if interval2.start > interval1.end: #no overlap, keep order
            answer = 0, interval1, interval2
            return answer
        else:                               # overlap, combine
            new = Interval(minmin, maxmax)
            answer = 2, new
            return answer
    else:                                   # interval2 has earlier start
        if interval1.start > interval2.end: # no overlap, reverse order
            answer = 1, interval2, interval1
            return answer
        else:                               # overlap, combine
            new = Interval(minmin, maxmax)
            answer = 2, new
            return answer

def merge(intervals):
    # Parameters:
    #   intervals is a list of Intervals (see definition of interval above)
    # Output:
    #   list of Intervals after merging all intersecting intervals, sorted by start

    # Questions:
    #   Is the input list sorted?
    #   Is start always < end in an interval?

    # Test Cases:
    #   No intervals returns empty list
    #   1 interval returns that interval
    #   Intervals that have the same start and end
    #

    # Example:
    # Input:
    #   [[1,3],[2,6],[8,10],[15,18]]
    # Output:
    #   [[1,6],[8,10],[15,18]]
    result = []

    if len(intervals) < 2:
        return intervals

    for interval in intervals:
        if interval.start > interval.end:
            interval = Interval(interval.end, interval.start)
    intervals.sort(key = lambda x: x.start, reverse = False)

    for index, each in enumerate(intervals):
        if index == 0:
            result.append(each)
            continue
        try_merge = mergetwo(result[-1], each)
        if try_merge[0] == 0:      # Unchanged: not overlapping and in correct order
            result.append(each)
            continue
        elif try_merge[0] == 1:    # each is less and not overlapping??
            result.insert(len(result) - 1, try_merge[1])
            continue
        elif try_merge[0] == 2:    # try_merge is overlapping and merged
            result[-1] = finalMerge

    return result


## Arrangement
### Largest Number
def sig_larger(one, two):
    one_larger = int(''.join(one + two))
    two_larger = int(''.join(two + one))
    if one_larger > two_larger:
        return 1
    elif one_larger == two_larger:
        return 0
    elif one_larger < two_larger:
        return -1

def largestNumber(A):
    # NOTE: Solution requires Python 2 not Python 3
    # Parameters:
    #   A is an array of integers (can be very large)
    # Output:
    #   Return a string which is the largest formed by concatenating the integers

    # Test Cases:
    #   Empty array --> ''
    #   One element --> that element as a String
    #   Some integers with 2 digits
    #   Some integers with 3 digits
    #   Negative input?
    #   All integers the same

    # Example:
    # Input:
    #   [3, 30, 34, 5, 9]
    # Output:
    #   9534330
    answer = ''
    answerArr = []
    B = []

    for each in A:
        s = str(each)
        l = list(s)
        B.append(l)

    B.sort(cmp = sig_larger,reverse = True)

    for each in B:
        start = 0
        for item in each:
            if item == 0:
                start += 1
                continue
            elif item != 0:
                break
        if start == len(each):
            each = 0
        else:
            each = each[start:]
        temp = ''.join(each)
        answerArr.append(temp)

    start = 0
    for item in answerArr:
        if item == '0':
            start += 1
            continue
        elif item != '0':
            break
    if start == len(answerArr):
        answerArr = ['0']
    else:
        answerArr = answerArr[start:]
    answer = ''.join(answerArr)
    return answer


## Space Recycle
### First Missing Integer



# STRINGS
## Parsing
### Atoi
def atoi(A):
    # Parameters:
    #   A String, may include whitespace. Ignore whitespace before the number,
    #   ignore garbage after the number.
    # Output:
    #   An integer, positive or negative
    #   If no numeric character is found, return 0.
    #   If integer overflows, return INT_MAX is positive, otherwise INT_MIN
    #   INT_MAX is 2147483647 (32-bit integer), INT_MIN is -2147483648

    # Approach:
    #   Delete leading whitespace
    #
    # Examples:
    # Input:
    #   "9 2704"
    # Output:
    #   9
    start = 0
    numArr = []
    numStr = ''
    result = 0
    multiplier = 1
    char_digit = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,  '6':6, '7':7, '8':8,  '9':9}

    for index in range(len(A)):
        if A[index] == ' ':
            start += 1
        else:
            break

    for idx, item in enumerate(A[start:]):
        if (item == '+' and A[idx + 1] in '0123456789'):
            continue
        elif item in '0123456789' or (item == '-' and A[idx + 1] in '0123456789'):
            numArr.append(item)
        else:
            break

    numStr = ''.join(numArr)
    if len(numStr) == 0:
        return 0
    else:
        for digit in numStr[::-1]:
            if digit == '-':
                result = -result
            else:
                result += char_digit[digit] * multiplier
                multiplier *= 10
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648

    return result


## String Math
### Roman to integer
def romanToInt(A):
    # Parameters:
    #   A is a string of roman numerals
    #   The value of the roman numerals will be between 1(I)-3999 (MMMCMXCIX) since
    #   for 4000 and above there are other notations involved
    # Output:
    #   An integer equivalent to the roman numeral

    # Example:
    # Input:
    #   XIV
    # Output:
    #   14
    # Input:
    #   XX
    # Output:
    #   20

    roman_decoder = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reverse_roman = A[::-1]
    last = 0
    result = 0

    for letter in reverse_roman:
        current = roman_decoder[letter]
        if current < last:
            result -= current
        else:
            result += current
            last = current

    return result
