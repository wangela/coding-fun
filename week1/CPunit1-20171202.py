def summation(numbers):
    # Parameters:
    #   numbers is an array of positive integers < 10^4 in size
    # Output:
    #   an integer, the sum of all the numbers in the array
    sum = 0

    for each in numbers:
        sum += each

    return sum


def maxLength(a, k):
    # Parameters:
    #   a is an array of positive integers < 10^5 in length with each element <= 10^3
    #   k is an integer <= 10^9
    # Output:
    #   an integer, the length of the longest subarray whose elements sum to <= k
    # Perform:
    #   a is immutable, so you can't re-order its elements
    #   find the longest subarray with elements that sum to <= k

    # Track the longest
    longest = 0

    # Set the starting indexes for start and end pointers
    start = 0
    end = start
    count = 0
    curr = a[start]

    # Begin growing subarrays
    while end < len(a):
        print ("new: start", start, "end", end)
        # Add to the right until we overrun k
        while (curr <= k):
            # Count a successful addition
            count += 1
            # Check for max; since a[i] > 1, max length = is k
            if count == k:
                return count
            # Add to the right unless we've hit the end of array
            end += 1
            if end < len(a):
                curr += a[end]
                print ("growing: start", start, "end", end, "curr", curr, "count", count)
            else:
                break
        # Check for longest
        longest = max(longest, count)
        # Subtract from the left until we are back under k
        while (curr > k and start < end):
            curr -= a[start]
            start += 1
            count -= 1
            print ("shrinking: start", start, "end", end, "curr", curr)
        # If we are both at an element that > k, we will need to advance both
        if start == end:
            start += 1
            end += 1
            count = 0

    # If subarray length is longer than longest so far, replace longest
    longest = max(longest, count)

    return longest

    # NAIVE: O(n^2) time
    # for i in range(len(a)):
    #     # Set the max sum and starting index
    #     x = k
    #     idx = i
    #     curr = a[idx]
    #     count = 0
    #     while(x - curr >= 0 and idx < len(a)):
    #         # Count a successful subtraction
    #         x -= curr
    #         count += 1
    #         # Check for max; since a[i] > 1, max length = is k
    #         if count == k:
    #             return count
    #         # Increment for the next loop
    #         idx += 1
    #         if idx < len(a):
    #             curr = a[idx]
    #         else:
    #             break
    #
    #     # If subarray length is longer than longest so far, replace longest
    #     longest = max(longest, count)
    #
    # return longest

def longestSubsequence(x, y):
    # convert strings to dicts
    dx = {}
    dy = {}
    for character in x:
        if character not in dx:
            dx[character] = 1
        else:
            dx[character] += 1
    for char in y:
        if char not in dy:
            dy[char] = 1
        else:
            dy[char] += 1

    count = 0

    for item in dx.keys():
        if item in dy.keys():
            count += min(dx[item], dy[item])

    return count
