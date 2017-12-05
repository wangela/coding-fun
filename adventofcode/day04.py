def check_pass(phrases):
    phraseArr = phrases.splitlines()
    valid = len(phraseArr)
    print(valid)
    invalid = 0

    for each in phraseArr:
        check = set()
        phrase = each.split()
        for word in phrase:
            if word in check:
                invalid += 1
                break
            else:
                check.add(word)

    print(invalid)
    return valid - invalid

def check_pass_anagrams(phrases):
    phraseArr = phrases.splitlines()
    valid = len(phraseArr)
    print(valid)
    invalid = 0

    for each in phraseArr:
        check = set()
        phrase = each.split()
        for word in phrase:
            wordArr = list(word)
            wordArr.sort()
            dorw = tuple(wordArr)
            if dorw in check:
                invalid += 1
                break
            else:
                check.add(dorw)

    print(invalid)
    return valid - invalid
