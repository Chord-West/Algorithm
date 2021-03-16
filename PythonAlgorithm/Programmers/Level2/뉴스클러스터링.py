import math


def solution(str1, str2):
    answer = 0
    s1 = dict()
    s2 = dict()
    for i in range(1, len(str1)):
        tmp = str1[i - 1] + str1[i]
        if tmp.isalpha():
            tmp = tmp.lower()
            s1[tmp] = s1.get(tmp, 0) + 1
    for i in range(1, len(str2)):
        tmp = str2[i - 1] + str2[i]
        if tmp.isalpha():
            tmp = tmp.lower()
            s2[tmp] = s2.get(tmp, 0) + 1
    com = 0
    s1s = sum(x for x in s1.values())
    s2s = sum(x for x in s2.values())
    for k, v in s1.items():
        s2[k] = s2.get(k, 0)
        com += min(s2[k], v)
    sg = s1s + s2s - com
    tmp = 0
    if sg == 0:
        tmp = 1
    else:
        tmp = com / sg

    answer = math.floor(tmp * 65536)

    return answer