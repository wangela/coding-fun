def password_proof(pws):
    unused = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    next_candidates = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    answer = ""
    while len(unused) > 0:
        try_char = unused.pop()
        try:
            next_candidates.remove(try_char)
        except KeyError as e:
            print "first" + e
        for password in pws:
            if len(password) == 1:
                return "IMPOSSIBLE"
            elif password[0] == try_char:
                not_next_char = password[1]
                try:
                    next_candidates.remove(not_next_char)
                except:
                    answer += try_char
                    for each in unused:
                        answer += each
                    if len(answer) != 26:
                        return "IMPOSSIBLE"
                    else:
                        return answer
        if len(next_candidates) == 0 and len(answer) == 25:
            answer += try_char
        elif len(next_candidates) == 0 and len(answer) != 25:
            return "IMPOSSIBLE"
        else:
            next_char = next_candidates.pop()
            try:
                unused.remove(next_char)
            except KeyError as remerr:
                print "third" + remerr
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
