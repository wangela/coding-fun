def password_proof(pws):
    unused = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    next_candidates = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    backup = set()
    current_index = 0
    answer = ""
    while len(unused) > 0:
        try_char = unused.pop()
        next_candidates.discard(try_char)
        for password in pws:
            if len(password) == 1:
                return "IMPOSSIBLE"
            elif password[0] == try_char:
                not_next_char = password[1]
                next_candidates.discard(not_next_char)
        if len(next_candidates) == 0 and len(answer) == 25:
            answer += try_char
        elif len(next_candidates) == 0 and len(answer) != 25:
            return "IMPOSSIBLE"
        else:
            next_char = next_candidates.pop()
            unused.discard(next_char)
            answer += try_char + next_char
            next_candidates = set(unused)
    if len(answer) != 26:
        return "IMPOSSIBLE"
    else:
        return answer

def driver():
    t = int(raw_input())
    for i in range(1, t + 1):
        n = int(raw_input())
        passwords = [str(s) for s in raw_input().split(" ")]
        result = password_proof(passwords)
        print("Case #{}: {}".format(i, result))

driver()
