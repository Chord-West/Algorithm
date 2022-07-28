def solution(numbers, target):
    answer = 0
    size = len(numbers)
    ch = [0] * size;

    def dfs(L, S):
        nonlocal answer
        if L == size:
            if S == target:
                answer += 1
            return
        else:
            dfs(L + 1, S + numbers[L])
            dfs(L + 1, S - numbers[L])

    dfs(0, 0)

    return answer