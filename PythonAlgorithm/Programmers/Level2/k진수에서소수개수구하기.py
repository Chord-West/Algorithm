def solution(n, k):
    answer = 0
    # 진법 변환
    prime = [[0] * (n)]
    for i in range(2, n + 1):
        if prime[i] == 0:
            for j in range(j * 2, n, j):
                prime[j] = 1
    for x in subin(n, k).split('0'):
        if prime[int(x, k)] == 0:
            answer += 1
    return answer


def subin(n, k):
    s = ''
    while n > 0:
        s += str(n % k)
        n = n // k
    while '00' in s:
        s = s.replace('00', '0')
    return s[::-1]

