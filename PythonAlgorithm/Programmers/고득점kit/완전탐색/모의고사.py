def solution(answers):
    answer = []

    su1 = [1, 2, 3, 4, 5] * 2000
    su2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1500
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    sa = [0, 0, 0]
    for i in range(len(answers)):
        if su1[i] == answers[i]:
            sa[0] += 1
        if su2[i] == answers[i]:
            sa[1] += 1
        if su3[i] == answers[i]:
            sa[2] += 1

    _max = max(sa)
    for k, v in enumerate(sa):
        if _max == v:
            answer.append(k + 1)

    return answer