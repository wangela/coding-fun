def central(l, names):
    can_be_center = ["YES"] * 3
    first = names[0]
    second = names[1]
    third = names[2]
    match = ""
    odd = ""
    odd_index = -1

    for letter in range(l):
        if odd:
            # print("odd loop")
            test_match = [""] * 3
            compare_indexes = []
            for i in range(3):
                if i == odd_index:
                    continue
                else:
                    compare_indexes.append(i)
                    # print("index {}".format(i))
                    if names[i][letter] == odd:
                        test_match[i] = "ODD"
                        # print("at letter {}, {} matches odd {}".format(letter, i, odd))
                    elif names[i][letter] == match:
                        test_match[i] = "MATCH"
                        # print("at letter {}, {} matches match".format(letter, i, match))
                    else:
                        test_match[i] = names[i][letter]
            if len(compare_indexes) == 2 and test_match[compare_indexes[0]] == test_match[compare_indexes[1]]:
                continue
            elif test_match.count("ODD") == 1 and test_match.count("MATCH") == 1:
                extreme_index = test_match.index("MATCH")
                can_be_center[extreme_index] = "NO"
                # print("extreme no")
                break
            else:
                break
        if first[letter] == second[letter] and first[letter] != third[letter]:
            can_be_center[2] = "NO"
            match = first[letter]
            odd = third[letter]
            # print("odd: {}".format(odd))
            odd_index = 2
        elif third[letter] == second[letter] and third[letter] != first[letter]:
            can_be_center[0] = "NO"
            match = third[letter]
            odd = first[letter]
            # print("odd: {}".format(odd))
            odd_index = 0

    return can_be_center

def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        L = int(raw_input())
        names = [str(s) for s in raw_input().split(" ")]
        result = central(L, names)
        print("Case #{}: {} {} {}".format(i, result[0], result[1], result[2]))

driver()
