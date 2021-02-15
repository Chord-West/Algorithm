def solution(s):
    answer = ""
    idx = 0
    for i in s:
        if i.isalpha():
            idx += 1
            if idx % 2 != 0:
                answer += i.upper()
            else :
                answer += i.lower()
        else:
            idx = 0
            answer += ' '
            continue

    return answer