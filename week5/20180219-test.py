from collections import deque
# Question 1
def canReach(x1, y1, x2, y2):
    # Parameters: x1, y1 are the source coordinates and x2, y2 are the goal coordinates
    # Perform: Binary tree graph where from node x1, y1 you can either visit x1+y1, y1 or x1, x1+y1
    # Output: "Yes" if x2, y2 can be reached and "No" if it cannot be reached
    q = deque([(x1, y1)])
    visited = set((x1, y1))
    goal = (x2, y2)

    while q:
        node = q.popleft()
        if node == goal:
            return "Yes"
        if node not in visited:
            visited.add(node)
            left = (node[0] + node[1], node[1])
            right = (node[0], node[0] + node[1])
            if left == goal or right == goal:
                return "Yes"
            if left not in visited and left[0] <= x2 and left[1] <= y2:
                q.append(left)
            if right not in visited and right[0] <= x2 and right[1] <= y2:
                q.append(right)
    return "No"

# Question 2
def findNeighbors(i, j, m, visited):
    n = len(m)
    ivals = []
    jvals = []
    toVisit = []
    if (i - 1) >= 0:
        ivals.append(i - 1)
    if (i + 1) < n:
        ivals.append(i + 1)
    if (j - 1) >= 0:
        jvals.append(j - 1)
    if (j + 1) < n:
        jvals.append(j + 1)

    for x in ivals:
        if m[x][j] == 1 and (x, j) not in visited:
            toVisit.append((x, j))
    for y in jvals:
        if m[i][y] == 1 and (i, y) not in visited:
            toVisit.append((i, y))

    return toVisit

def walk(i, j, m, visited, s):
    s.append((i, j))
    group = 0
    s.extend(findNeighbors(i, j, m, visited))

    while s:
        node = s.pop()
        print(node)
        x = node[0]
        y = node[1]
        if (x, y) in visited:
            continue
        if m[x][y] == 1:
            group += 1
            s.extend(findNeighbors(x, y, m, visited))
            visited.add((x, y))

    return (group, visited)

def countGroups(m, t):
    # Parameters: m is an nxn matrix of values 0 or 1. t is a list of integers representing group sizes to count in m.
    # Perform: Two locations are in the same group if |x1 - x2| + |y1 - y2| = 1 and both cells contains the value 1
    # Output: A list of the number of groups of each size requested in t.
    ret = []
    sizeCount = dict()
    visited = set()
    s = []

    for i in range(len(m)):
        for j in range(len(m)):
            if (i, j) in visited:
                continue
            elif m[i][j] == 1:
                totalGroup = walk(i, j, m, visited, s)
                groupSize = totalGroup[0]
                #print("group size found: {}".format(groupSize))
                visited = totalGroup[1]
                if groupSize in sizeCount:
                    sizeCount[groupSize] += 1
                else:
                    sizeCount[groupSize] = 1

    for k in t:
        if k in sizeCount:
            ret.append(sizeCount[k])
        else:
            ret.append(0)

    return ret

def driver2():
    n1 = int(raw_input())
    n2 = int(raw_input())
    m1 = [0] * n1
    m = []
    for x in range(n2):
        m.append(list(m1))
    for i in range(n1):
        mrow = [int(s) for s in raw_input().split()]
        for j in range(n2):
            m[i][j] = mrow[j]
    for x in range(n1):
        print(m[x])
    q = int(raw_input())
    t = []
    for k in range(q):
        t.append(int(raw_input()))
    print(t)
    result = countGroups(m, t)
    print(result)
    return result

# Question 3
def countFriends(student, friends):
    visited = set()
    q = deque([student])
    numFriends = 0
    friendList = set([student])

    while q:
        current = q.popleft()
        if current not in visited:
            visited.add(current)
            numFriends += 1
            #print(friends[current])
            for each in (friends[current] - visited):
                q.append(each)
                friendList.add(each)
    #print("student {} has {} friends".format(student + 1, numFriends))
    #print(friendList)
    return friendList

def getTheGroups(n, queryType, studs1, studs2):
    students1 = []
    students2 = []
    for each in studs1:
        students1.append(each - 1)
    for each in studs2:
        students2.append(each - 1)

    totals = []
    friends = []
    for each in range(n):
        friends.append(set([each]))

    for qnum, q in enumerate(queryType):
        s1 = students1[qnum]
        s2 = students2[qnum]
        if q == "Friend":
            friends[s1].add(s2)
            friends[s2].add(s1)
            #print(friends)
        elif q == "Total":
            total = set.union(countFriends(s1, friends), countFriends(s2, friends))
            #print(total)
            totalCount = len(total)
            totals.append(totalCount)

    return totals

def driver3():
    n = int(raw_input())

    queryType_cnt = 0
    queryType_cnt = int(raw_input())
    queryType_i = 0
    queryType = []
    while queryType_i < queryType_cnt:
        try:
            queryType_item = str(raw_input())
        except:
            queryType_item = None
        queryType.append(queryType_item)
        queryType_i += 1


    students1_cnt = 0
    students1_cnt = int(input())
    students1_i = 0
    students1 = []
    while students1_i < students1_cnt:
        students1_item = int(raw_input())
        students1.append(students1_item)
        students1_i += 1


    students2_cnt = 0
    students2_cnt = int(input())
    students2_i = 0
    students2 = []
    while students2_i < students2_cnt:
        students2_item = int(raw_input())
        students2.append(students2_item)
        students2_i += 1


    res = getTheGroups(n, queryType, students1, students2);
    for res_cur in res:
        print( str(res_cur) + "\n" )

driver3()
