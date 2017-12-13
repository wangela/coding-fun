def convert_characters_to_bytes(s):
    numbers = 0
    return numbers

def hashKnot(lengths):
    special = convert(lengths)

    arr = []
    current = 0
    skip = 0

    for i in range(256):
        arr.append(i)

    for each in lengths:
        if each > 256:
            continue
        if each != 1:
            for i in range(each//2):
                index = (current + i) % 256
                reverse = (current + each - 1 - i) % 256
                temp = arr[index]
                arr[index] = arr[reverse]
                arr[reverse] = temp
        current += each + skip
        skip += 1

    product = arr[0] * arr[1]
    return product

def reverseList(list, each):
    current = 0
    arr = list
    for i in range(each//2):
        index = current + i
        reverse = current + each - 1 - i
        temp = arr[index]
        arr[index] = arr[reverse]
        arr[reverse] = temp

    return arr
