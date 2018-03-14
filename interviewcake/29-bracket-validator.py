def validator(A):
    # Parameter: A is a string with opening and closing brackets, braces, and parens
    # Perform: Validate whether openers and closers are properly nested
    # Output: Return True if valid and False if not
    openers = {'[', '{', '('}
    closers = {']': '[','}': '{', ')': '('}

    bracket_q = []

    for c in A:
        if c in openers:
            bracket_q.append(c)
        if c in closers:
            match_bracket = closers[c]
            if len(bracket_q) == 0:
                return False
            last_opened = bracket_q.pop()
            if match_bracket == last_opened:
                continue
            else:
                return False

    if len(bracket_q) > 0:
        return False
    else:
        return True
