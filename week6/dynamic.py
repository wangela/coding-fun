def maxProduct(A):
    # Parameter: A is a list
    # Perform: Find a subarray with at least 1 number with the largest product
    # Output: The max product
    # Example: [2, 3, -2, 5] -> [2, 3] -> 6
    #       [-4, 0, -5, 0] -> [0] -> 0
    if len(A) == 0:
        return None

    answer = A[0]

    products = [answer]
    current_positive_max = 1
    current_negative_min = 1
    if len(A) > 1:
        for x in A[1:]:
            last = products[-1]
            if x == 0:
                products.append(max(current_negative_min, current_positive_max, x))
                current_positive_max = 1
                current_negative_min = 1
                if x > answer:
                    answer = x
            elif x > 0:
                current_positive_max *= x
                current_negative_min *= x
                if current_positive_max > answer:
                    answer = current_positive_max
            else: # x < 0
                temp = current_positive_max
                current_positive_max = max(x * current_negative_min, 1)
                current_negative_min = x * temp
                if current_positive_max > 1:
                    if current_positive_max > answer:
                        answer = current_positive_max

    return answer

def numDecodings(A):
    # Parameter: A is an encoded string
    # Perform: Identify how the string could be decoded if 'A' -> '1', ... 'Z' -> '26'
    # Output: Integer, the number of ways to decode the message
    if len(A) == 0:
        return 0

    combos = []
    doubles = {'1': '0123456789', '2': '0123456'}
    last = '0' # The digit preceding the current one
    penultimate = False # Is this the third in a 3-digit string where digits 1 and 2 are both 1 or 2?

    for index, digit in enumerate(A):
        if index == 0:
            current_combos = 1
        else:
            current_combos = combos[index - 1]
        if digit == '0':
            if last not in '12':
                return 0
            elif penultimate == True:
                current_combos /= 2
                penultimate = False
            else:
                penultimate = False
        elif last == '1' or last == '2':
            if digit in doubles[last]:
                current_combos *= 2
                if penultimate == True:
                    current_combos = combos[index - 1] + combos[index - 2]
                penultimate = True
            else:
                penultimate = False
        else:
            penultimate = False
        # print("{}, last = {}, penultimate = {}, combo count = {}".format(index, last, penultimate, current_combos))
        combos.append(current_combos)
        last = digit

    return combos[-1]
