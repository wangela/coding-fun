def captcha(A):
    answer = 0
    for index, each in enumerate(A):
        next = A[0]
        if index != len(A) - 1:
            next = A[index + 1]
        if each == next:
            answer += int(each)

    return answer

def captcha2(A):
    answer = 0
    for index, each in enumerate(A):
        next = A[len(A)/2 + index - len(A)]
        if each == next:
            answer += int(each)

    return answer
