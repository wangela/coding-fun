def checksum(A):
    # A = array of arrays
    # For each row, calculate difference between largest and smallest numbers
    # Add up the differences from each row to generate and return the checksum
    sum = 0

    for row in A:
        difference = -1
        largest = row[0]
        smallest = row[0]
        for item in row[1:]:
            if item > largest:
                largest = item
            if item < smallest:
                smallest = item
        difference = largest - smallest
        sum += difference

    return sum

def convert(A):
    x = [[int(i) for i in s.split()] for s in A.splitlines()]

    return x

def checkdiv(A):
    # A = array of arrays
    # For each row, find the two numbers that are evenly divisible and divide
    # Add up the divisions from each row to generate and return the checkdiv
    sum = 0

    for row in A:
        difference = -1
        numerator = row[0]
        denominator = row[0]
        dindex = 0
        found = False
        for index, item in enumerate(row):
            if index == dindex:
                continue
            numerator = item
            idx = index
            while (max(numerator, denominator) % min(numerator, denominator) != 0):
                if idx < len(row) - 1:
                    idx += 1
                    numerator = row[idx]
                    continue
                else:
                    break
            if (max(numerator, denominator) % min(numerator, denominator) == 0):
                if numerator < denominator:
                    temp = numerator
                    numerator = denominator
                    denominator = temp
                break
            else:
                denominator = item
                dindex = index
        div = numerator / denominator
        print numerator, denominator, div
        sum += div

    return sum
