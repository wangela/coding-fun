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
