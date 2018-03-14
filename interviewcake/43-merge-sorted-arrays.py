def mega_order(mine, alices):
    # Parameters: mine and alices are sorted lists of order IDs.
    # Perform: combine the two lists into a single larger sorted list
    # Output: The combined sorted list
    answer = []

    while mine or alices:
        if not mine:
            answer.extend(alices)
            break
        elif not alices:
            answer.extend(mine)
            break
        if mine[0] < alices[0]:
            answer.append(mine[0])
            mine.pop(0)
        else:
            answer.append(alices[0])
            alices.pop(0)

    return answer
