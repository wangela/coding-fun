from collections import deque

def sale_labels(unsorted_labels):
    sale = []
    # unsorted_labels.sort()
    # regular = []
    # unsorted = set(unsorted_labels)
    unsorted_queue = deque(unsorted_labels)

    while len(unsorted_queue) > 0:
        # largest = unsorted_labels.pop()
        smallest = unsorted_queue.popleft()
        # largest_on_sale = 0.75 * largest
        smallest_regular = 4 * smallest / 3
        try:
            unsorted_queue.remove(smallest_regular)
        except ValueError as e:
            print e
        sale.append(smallest)
    return sale

def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        n = int(raw_input())
        all_labels = [int(s) for s in raw_input().split(" ")]
        result = sale_labels(all_labels)
        answer = ""
        for each in result:
            answer += str(each) + " "
        print("Case #{}: {}".format(i, answer[:-1]))

driver()
