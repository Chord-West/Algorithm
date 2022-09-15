def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        S = 0
        j = i

        while S < n:
            S += j
            j += 1
        if S == n:
            answer += 1
    return answer