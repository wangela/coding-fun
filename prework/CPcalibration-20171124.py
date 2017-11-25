def winner(andrea, maria, s):
    n = len(andrea) # Assume andrea and maria have equal length
    first = 0    # Default is to go after even indices.
    aScore = 0
    mScore = 0
    score = 0
    if s == "Odd":
        first = 1

    for x in range(first, n, 2):
        score = andrea[x] - maria[x]
        print("x =", x, "score =", score)
        aScore += score
        mScore -= score

    if aScore > mScore:
        return "Andrea"
    elif aScore < mScore:
        return "Maria"
    else:                   # aScore = mScore
        return "Tie"

def braces(values):
    result = []
    leftBraces = {'(', '{', '['}
    rightBraces = {')', '}', ']'}

    for eachString in values:
        leftStack = []
        stringPassed = True
        for eachChar in eachString:
            if eachChar in leftBraces:
                leftStack.append(eachChar)
            elif eachChar in rightBraces:
                if leftStack:
                    lastLeft = leftStack.pop()
                    if matched(lastLeft, eachChar):
                        continue        #balanced so far
                    else:               #unbalanced: doesn't match last left brace
                        stringPassed = False
                        break
                else:                   #unbalanced: closing brace before opening
                    stringPassed = False
                    break
        if (len(leftStack) == 0 and stringPassed):
            result.append("YES")
        else:                           #unbalanced: leftover left braces
            result.append("NO")

    return result

def matched(left, right):
    if (left == '{' and right == '}') or (left == '(' and right == ')') or (left == '[' and right == ']'):
        return True
    else:
        return False


def arrangeCoinsBruteForce(coins):
    for c in coins:
        m = 1
        if c < m:       # shouldn't happen, as problem states 1 <= coins[i]
            print(0)
        else:
            while c >= m:
                c -= m
                m += 1
            print(m - 1)

def arrangeCoins(coins):
    for c in coins:
        # Find row where sum of all integers 1 to m <= c
        # Formula for sum of all integers is m*(m+1)/2 = m^2 + m / 2
        # c * 2 = m^2 + m + 0
        # sqrt(c*2) should approximate m for us and give us an intelligent guess

        testM = math.floor(math.sqrt(c*2))
        m = testM - 1
        testCoins = m*testM/2
        c -= testCoins

        if c < m:
            print(m)
        else:
            while c >= m:
                m += 1
                c -= m
            if c >= 0:
                print(m)
            else:
                print(m - 1)


def degreeofArray(arr):
    members = {}

    # Catalog a dictionary of each integer tracking count, indexes of occurrence, and size of the subarray
    for index, item in enumerate(arr):
        if item in members:
            print("duplicate for", item)
            members[item][count] += 1
            members[item][index].append(index)
            indices = members[item][index]
            members[item][size] = indices[-1] - indices.first[0]
        else:
            members[item] = {'count': 1, 'indexes': [index], 'size': 1}

    # Identify the key(s) with the max count to get the degree of the array

    # Among the key(s) with the max count, identify the minimum size of the subarray

    # return that minimum size
