def findNumber(arr, k):
    for each in arr:
        if each == k:
            return "YES"

    return "NO"

def oddNumbers(l, r):
    odds = []
    if l % 2 == 0:
        l += 1
    for i in range (l, (r + 1), 2):
        odds.append(i)

    return odds
