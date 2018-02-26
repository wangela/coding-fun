### Ashley Loves Numbers
def does_not_repeat(x):
    if x % 11 == 0:
        return False
    y = x
    while y % 100 != y:
        z = y % 100
        if z % 11 == 0:
            return False
        y -= y % 10
        y //= 10
    return True

def countNumbers(arr):
    # Parameter: arr is a 2D array of integers containing q rows of (n, m) values
    # Perform: For each row in arr, count the number of integers n <= i <= m that
    #   do NOT contain repeating digits
    # Output: For each row, print an integer representing the count of integers
    #   between n and m inclusive that do not have repeating digits.
    # Example: [[1, 20], [9, 19]] -> 19/n10
    #       [[7, 8], [52, 80], [57, 64], [74, 78]] -> 2/n26/n8/n4
    for row in arr:
        ashley_count = 0
        n = row[0]
        m = row[1]
        for x in range(n, m + 1):
            if does_not_repeat(x):
                ashley_count += 1
        print(ashley_count)

### Most Frequent Substring
def getMaxOccurrences(s, minLength, maxLength, maxUnique):
    # Example: "abcde", 2, 4, 26 -> "ab" x 1, "bc" x 1,"cd" x 1, "de" x 1 -> 1
    #   "ababab", 2, 3, 4 -> "ab" x 3, "aba" x 2, "bab" x 2, "ba" x 2 -> 3
    subs = dict()

    for start_index in range(len(s) - minLength + 1):
        sub = s[start_index:start_index + minLength]
        uniques = set()
        for character in sub:
            if character not in uniques:
                uniques.add(character)
        if len(uniques) > maxUnique:
            continue
        if sub in subs:
            subs[sub] += 1
        else:
            subs[sub] = 1

    occurrences = []
    for substring in subs.keys():
        occurrences.append(subs[substring])

    if len(occurrences) > 0:
        return max(occurrences)
    else:
        return 0

### Budget Shopping
def budgetShopping(n, bundleQuantities, bundleCosts):
    # Knapsack problem with costs
    # Example: 13, [5, 2], [2, 1] -> 5(2) + 5(2) + + 5(2) + 5(2) + 5(2) + 5(2) + 2(1) -> 32 notebooks for $12
    #       50, [20, 19], [24, 20] -> 20(24) + 20(24) -> 40 notebooks for $48
    #       4, [10], [2] -> 10(2) + 10(2) -> 20 notebooks for $4
    max_notebooks = dict()
    num_shops = len(bundleQuantities)
    min_cost = min(bundleCosts)
    max_notebooks[0] = 0

    for i in range(1, n + 1):
        comparison_shop = []
        max_purchase = 0
        for shop in range(num_shops):
            if i >= bundleCosts[shop]:
                remaining = i - bundleCosts[shop]
                purchase = bundleQuantities[shop]
                if remaining in max_notebooks:
                    purchase += max_notebooks[remaining]
                comparison_shop.append(purchase)
        if len(comparison_shop) > 0:
            max_purchase = max(comparison_shop)
        max_notebooks[i] = max(max_purchase, max_notebooks[i - 1])

    return max_notebooks[n]
