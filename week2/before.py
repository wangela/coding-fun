# HASHING
## Key Formation
### Anagrams
def anagrams(A):
    # Parameters:
    #   A is an array of strings
    # Output:
    #   A list of all groups of strings that are anagrams.
    #   Represent a group as a list of integers representing the 1-based index
    #   of the string in the original array.
    # Example:
    #   ["cat", "dog", "god", "tca"] -> [[1,4], [2,3]]

    unique = {}
    result = []

    for index, each in enumerate(A):
        word = list(each)
        word.sort()
        dorw = tuple(word)
        if dorw in unique:
            unique[dorw].append(index + 1)
        else:
            unique[dorw] = [index + 1]

    for item in unique.keys():
        arr = unique[item]
        result.append(arr)

    return result


## Hash Search
### 2 Sum
def twoSum(A, B):
    # Parameters:
    #   A is a tuple of integers
    #   B is an integer
    # Output:
    #   Return a list of integers
    #   The list should have the indices of two numbers from A that add up to B
    #   Index 1 < Index 2
    #   Indices are 1-based not 0-based
    #   If multiple solutions exist, return the one where index 2 is minimum
    #   If multiple soulutions exist using index 2, choose where index 1 is minimum
    # Example:
    #   [2, 7, 11, 15] target = 9 --> [1, 2]

    # Test Cases:
    #   (0, 0) target = 0 --> [1, 2]
    #   (0, 1) target = 1 --> [1, 2]
    #   (1, 0) target = 1 --> [1, 2]
    #   (1, 1, 1, 1, 1) target = 2 --> [1, 2]
    #   (-2, 1, 11, 2, 7, 15) target = 9 --> [1,3]
    )

    # Approach:
    #   Convert the tuple to a dictionary with the integers as keys and the indices as values
    #   Test combos of keys to see which add up to the target
    #   Pick the lowest indices among the values for those keys
    #   Order the indices in the right order

    unique = {}
    result = []
    pairs = []

    for index, each in enumerate(A):
        if each in unique:
            unique[each].append(index + 1)
        else:
            unique[each] = [index + 1]

    for item in unique.keys():
        c = B - item
        pair = []
        if c in unique:
            pair.append(unique[c][0])
            if c == item:
                if len(unique[c]) > 1:
                    pair.append(unique[c][1])
                else:
                    continue
            else:
                pair.append(unique[item][0])
            pair.sort()
            pairs.append(pair)

    pairs.sort(key=lambda x: x[0])
    pairs.sort(key=lambda x: x[1])

    if len(pairs) > 0:
        return pairs[0]
    else:
        return pairs


# LINKED LISTS
## 
