def solution(s):
    cnt, idx = 0, 0
    while len(s) > 1:
        cnt += s.count('0')
        s = s.replace('0', '')
        s = binaryChange(len(s))
        idx += 1
    answer = [idx, cnt]

    return answer


def binaryChange(n):
    tmp = ''
    while n > 0:
        tmp += str(n % 2)
        n = n // 2
    return tmp[::-1]
