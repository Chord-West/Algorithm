def solution(numbers):
    def dfs(L, word):
        if L == n:
            num.add(int(word))
        else:
            for i in range(size):
                if ch[i] == 0:
                    ch[i] = 1
                    dfs(L + 1, word + numbers[i])
                    ch[i] = 0

    size = len(numbers)
    ch = [0] * size
    num = set()
    for n in range(1, size + 1):
        dfs(0, '')
    num -= set(range(0, 2))
    for i in range(2, 999999):
        num -= set(range(i * 2, 9999999, i))
    return len(num)