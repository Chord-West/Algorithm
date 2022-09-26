def solution(n, k):
    answer = 0
    # 진법 변환
    for x in change(n, k).split('0'):
        if len(x) == 0:
            continue
        i = int(x)
        sosu = True
        if i < 2:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                sosu = False
                break
        if sosu:
            answer += 1
    return answer


def change(n, k):
    s = ''
    while n > 0:
        s += str(n % k)
        n = n // k
    return s[::-1]

