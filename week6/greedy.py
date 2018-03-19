def canCompleteCircle(A, B):
    # Parameters: A is a tuple of integers representing the amount of gas at each station,
        # B is a tuple of integers with the cost of gas to travel to the next station
    # Output: An integer, the minimum index of the gas station to start at in
    #   order to get all around the circle (return to the gas station at this
    #   index). If impossible, return -1.
    length = len(A)
    sumOfGas = 0
    sumOfCost = 0

    for gas in A:
        sumOfGas += gas

    for cost in B:
        sumOfCost += cost

    if sumOfCost > sumOfGas:
        return -1
    else:
        minimum_index = 0

        while minimum_index < length:
            sumOfGas = 0
            sumOfCost = 0
            for i in range(length):
                current_index = (minimum_index + i) % length
                #print(current_index)
                sumOfGas += A[current_index]
                sumOfCost += B[current_index]
                if sumOfCost > sumOfGas:
                    minimum_index += i + 1
                    #print(minimum_index)
                    break
                elif i == length - 1:
                    return minimum_index
