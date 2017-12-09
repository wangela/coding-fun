def reallocate(A):
    # Parameters: A is an array with 16 integers
    # Perform: Take the index with the max value and redistribute one per following index until reaching zero
    # Output: Integer count of how many redistributions will happen until a configuration has been seen before
    # Example:
    #     With 4 memory banks [0, 2, 7, 0] -> [2,4,1,2] -> [3,1,2,3] -> [0,2,3,4] -> [1,3,4,1]-> [2,4,1,2] -> 5
    configurations = set()
    count = 0
    repeated = False

    while repeated == False:
        t = tuple(A)
        if t in configurations:
            repeated = True
            break
        else:
            configurations.add(t)
            count += 1
            max_value = max(A)
            max_index = A.index(max_value)
            A[max_index] = 0
            A = redistribute(A, max_index + 1, max_value)

    return count

def redistribute(A, start_index, blocks):
    for i in range(blocks):
        new_index = (start_index + i) % len(A)
        A[new_index] += 1
    return A

def convert(A):
    arr = A.split()
    intArr = []
    for each in arr:
        intArr.append(int(each))
    return intArr

def reallocate_count(A):
    # Parameters: A is an array with 16 integers
    # Perform: Take the index with the max value and redistribute one per following index until reaching zero
    # Output: Integer count of how many redistributions will happen until a configuration has been seen before
    # Example:
    #     With 4 memory banks [0, 2, 7, 0] -> [2,4,1,2] -> [3,1,2,3] -> [0,2,3,4] -> [1,3,4,1]-> [2,4,1,2] -> 5
    configurations = {}
    count = 0
    repeated = False
    cycle_length = 0

    while repeated == False:
        t = tuple(A)
        if t in configurations:
            cycle_length = count - configurations[t]
            repeated = True
            break
        else:
            configurations[t] = count
            count += 1
            max_value = max(A)
            max_index = A.index(max_value)
            A[max_index] = 0
            A = redistribute(A, max_index + 1, max_value)

    return cycle_length
