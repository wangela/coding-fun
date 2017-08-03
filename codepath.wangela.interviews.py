def rotateArray(a, b):
	ret = []
        shift = b % (len(a))
        print(shift)
        for i in xrange(len(a) - shift):
            ret.append(a[i + shift])
        for j in xrange(shift):
        	ret.append(a[j])
        return ret

def oneWaySearch(A, B, highFirst):
	low = 0
	high = len(A) - 1
	result = -1

	while (low <= high):
		mid = (high + low) / 2
		if (A[mid] == B):
			result = mid
			if highFirst:
				low = mid + 1
			else:
				high = mid - 1
		elif (B < A[mid]):
			high = mid - 1
		else:
			low = mid + 1
	return result

def searchRange(A, B):
	highIndex = oneWaySearch(A, B, True)
	if (highIndex == -1):
		return 0
	else:
		lowIndex = oneWaySearch(A, B, False)

	return (lowIndex, highIndex)

import heapq

def kthSmallest(A, k):
	myHeap = []
	result = -1

	for h in range(k):
		heapq.heappush(myHeap,A[h])
	for i in range(k, len(A)):
		heapq.heappush(myHeap,A[i])
		myHeap = myHeap[:k]
	for j in range(k):
		result = heapq.heappop(myHeap)
	return result

def naiveShallowRange(A, B, C):
    pivotCount = 0
    pSum = A[0]
    tempArr = []

    if (pSum <= C):
        if (pSum >= B):
            pivotCount += 1
        if (len(A) > 1):
        	tempArr = A[1:]
        	tempArr[0] += A[0]
        	pivotCount += naiveShallowRange(tempArr, B, C)

    return pivotCount


def naiveNumRange(A, B, C):
	pivotCount = 0
	pSum = A[0]
	tempArr = []

	while (len(A) > 1):
		if (pSum <= C):
			if (pSum >= B):
				pivotCount += 1
			tempArr = A[1:]
			tempArr[0] += A[0]
			pivotCount += naiveShallowRange(tempArr, B, C)
		A = A[1:]
		pSum = A[0]

	if (A[0] >= B and A[0] <= C):
		pivotCount += 1

	return pivotCount

def numRange(A, B, C):
	sumCount = 0

	for index, val in enumerate(A):
		if (val > C): continue
		if (val >= B):
			sumCount += 1
		currSum = val
		for j in A[(index + 1):]:
			currSum += j
			if (currSum > C): break
			if (currSum >= B):
				sumCount += 1
	return sumCount

def removeDuplicates(A):
	## remove duplicates from an array
	index = 0
	while index < (len(A) - 1):
		vi = A[index]
		j = A[index + 1]
		if j == vi:
			for vj in A[(index + 1):]:
				if vj == vi:
					A.pop(index + 1)
				else:
					break
		index += 1

	return len(A)

def fastRemoveDupes(A):
	## no pop function allowed (O(n) for pop means O(n^2) for 2-pointer function)
	uniqueIndex = 0
	dupCount = 0
	nextVal = A[0]
	for index, val in enumerate(A[:-1]):
		j = A[index + 1]
		if val < nextVal: 
			continue
		elif val == j:
			for idx, vj in enumerate(A[(index + 1):]):
				currDup = 0
				if vj == val:
					dupCount += 1
					currDup += 1
					if idx == len(A) - (index + 1) - 1:
						nextVal += 1
				else:
					uniqueIndex += 1
					nextVal = vj
					A[uniqueIndex] = nextVal
					break
		else:
			uniqueIndex += 1
			nextVal = j
			A[uniqueIndex] = nextVal

	if dupCount > 0:
		A = A[:-dupCount]

	return len(A)

def deleteDupes(A):
	## allow 2 or less of each element in a sorted array
	uniqueIndex = 0
	dupCount = 0
	nextVal = A[0]
	for index, val in enumerate(A[:-1]):
		j = A[index + 1]
		if val < nextVal: 
			continue
		elif val == j:
			currDup = 0
			for idx, vj in enumerate(A[(index + 1):]):
				if vj == val:
					currDup += 1
					if currDup == 1:
						uniqueIndex += 1
						A[uniqueIndex] = vj
					elif currDup > 1:
						dupCount += 1
					if idx == len(A) - (index + 1) - 1:
						nextVal += 1
				else:
					uniqueIndex += 1
					nextVal = vj
					A[uniqueIndex] = nextVal
					break
		else:
			uniqueIndex += 1
			nextVal = j
			A[uniqueIndex] = nextVal

	if dupCount > 0:
		A = A[:-dupCount]

	return len(A)

	## solution
    # n = len(A)
    # k = 0
    # i = 1
    # for i in range(2,n):
    #     if A[i] == A[i-k-1] and A[i] == A[i-k-2]:
    #         if i >= 2 and A[i-2] == A[i]:
    #             k += 1
    #     elif k > 0:
    #         A[i-k] = A[i]
    # A = A[:n-k]
    # return n-k

def searchArr(X, n, sought):
	new = {}
	print sought
	for index, item in enumerate(X[n:]):
		print item
		if item == sought:
			new[index + n] = item
			break
		elif item > sought:
			break
		else:
			continue
	return new


def intersectFinder(A, B):
	i = 0
	j = 0
	new = []
	while i < len(A) and j < len(B):
		if A[i] > B[j]:
			# print ('A')
			j += 1
		elif B[j] > A[i]:
			# print ('B')
			i += 1
		elif A[i] == B[j]:
			# print ('equal')
			new.append(A[i])
			i += 1
			j += 1
	return new

def longestCommonPrefix(A):
	lcp = ''
	i = 0
	flag = True

	if len(A) == 1:
		lcp = A[0]
		return lcp
	else:
		for letter in A[0]:
			lcp += letter
			for word in A[1:]:
				if i >= len(word):
					flag = False
					break
				else:
					if word[i] == lcp[-1]:
						continue
					else:
						flag = False
						break
			if flag == False:
				break
			else:
				i += 1
	if flag == False:
		lcp = lcp[:-1]

	return lcp

def lengthOfLastWord(A):
	lw = ''
	space = False

	for letter in A:
		if letter == ' ':
			space = True
			continue
		if space == True:
			lw = ''
			lw += letter
			space = False
		else:
			lw += letter

	return len(lw)

def removeElement(A, B):
	i = 0
	dupes = 0
	result = []

	for item in A:
		if item == B:
			dupes += 1
			continue
		else:
			A[i] = item
			i += 1
	if dupes > 0:
		A = A[:-dupes]

	result.append(i)
	result.append(A)
	return i

def sortColors(A):
	# red = 0, white = 1, blue = 2
	# Sort n objects so that objects of the same color are adjacent in the order red, white, blue
	i = 0
	result = []
	whiteCount = []
	blueCount = []

	for item in A:
		if item == 0:
			result.append(item)
			i += 1
		elif item == 1:
			whiteCount.append(item)
		elif item == 2:
			blueCount.append(item)
	result.extend(whiteCount)
	result.extend(blueCount)

	return result

def calcArea(m, n):
	width = abs(m[0] - n[0])
	height = min(m[1], n[1])

	return width * height

def maxArea(A):
	## fails if there are 2 instances of maxY
	i = 0
	m = [i, A[i]]
	maxY = max(A)
	maxX = 0
	pen = [0, A[i]]
	maxA = 0

	for index, val in enumerate(A[1:]):
		n = [index + 1, val]
		if val > pen[1] and val < maxY:
			pen = n
			print ('penX = ' + str(pen[0]) + ', penY = ' + str(pen[1]))
		elif val == maxY:
			maxX = index
		area = calcArea(n, pen)
		print ('area = ' + str(area))
		if area > maxA:
			maxA = area

	return maxA

def maxArea(A):
	m = [0, A[0]]
	n = [len(A) - 1, A[-1]]
	print n
	maxA = calcArea(m,n)

	if len(A) <= 2:
		return maxA
	elif m[1] < n[1]:
		area = maxArea(A[1:])
	else:
		area = maxArea(A[:-1])
	if area > maxA:
		maxA = area

	return maxA

def diffMax(A, B, C, d, e, f):
	diffAB = abs(A[d] - B[e])
	diffBC = abs(B[e] - C[f])
	diffCA = abs(C[f] - A[d])
	l = [diffAB, diffBC, diffCA]

	dMax = max( (l[i], i) for i in range(2))

	return dMax

def removeEnd(A, B, C, x, isMin):
	if isMin:
		if x = 0:
			if A[0] < B[0]:
				A = A[1:]
			else:
				B = B[1:]
		elif x = 1:
			if C[0] < B[0]:
				C = C[1:]
			else:
				B = B[1:]
		elif x = 2:
			if A[0] < C[0]:
				A = A[1:]
			else:
				C = C[1:]
	else:
		if x = 0:
			if A[-1] > B[-1]:
				A = A[:-1]
			else:
				B = B[:-1]
		elif x = 1:
			if C[-1] > B[-1]:
				C = C[:-1]
			else:
				B = B[:-1]
		elif x = 2:
			if A[-1] > C[-1]:
				A = A[:-1]
			else:
				C = C[:-1]

	return (A, B, C)

def minimize(A, B, C):
	## return the minimum possible max difference between indexed elements of 3 arrays
	i = 0
	j = 0
	k = 0

	maxDiff = diffMax(A, B, C, i, j, k)
	currMin = maxDiff[0]

	a = len(A) - 1
	b = len(B) - 1
	c = len(C) - 1

	maxDiff2 = diffMax(A, B, C, a, b, c)

	if maxDiff2[0] < maxDiff[0]:
		removeEnd(A, B, C, maxDiff[1], True)
	elif maxDiff[0] < maxDiff2[0]:
		removeEnd(A, B, C, maxDiff2[1], False)

	if maxDiff < currMin:
		currMin = maxDiff

	return currMin