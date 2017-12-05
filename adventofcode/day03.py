def shortestPath(n):
    # Parameters:
    #   n is a positive integer on a spiral square pattern
    # Output:
    #   Return the shortest path to get from n to 1 by moving up, down, left,
    #   and/or right according to the Manhattan Distance

    # Approach:
    #   Figure out which ring the integer is on (odd squares)
    #   Figure out the distance to the nearest axis (axes at 1x ring intervals)
    #   Add the two together to calculate the Manhattan Distance

    ringSteps = 0
    axisSteps = 0

    nRoot = math.floor(math.sqrt(n))
    ringRoot = nRoot
    if math.sqrt(n) != nRoot:
        ringRoot += 1
    if ringRoot % 2 != 1:
        ringRoot += 1
    print("ringRoot", ringRoot)
    ringSteps = math.floor(ringRoot / 2)
    print("ringSteps", ringSteps)

    axisArray = []
    first = (ringRoot - 2)**2 + 1
    axisArray.append(first)
    second = first + ringSteps - 1
    axisArray.append(second)
    for i in range(3):
        second += (ringSteps * 2)
        axisArray.append(second)
    last = ringRoot**2
    if last != axisArray[-1] + ringSteps:
        print("axisArray checksum doesn't match")
    else:
        print("all good for ring", ringSteps)
    axisArray.append(last)

    options = []
    for option in axisArray[1:5]:
        a = int(math.fabs(n - option))
        options.append(a)
    axisSteps = min(options)
    print("axisSteps", axisSteps)

    totalSteps = ringSteps + axisSteps
    return totalSteps

def nextSquare(n):
