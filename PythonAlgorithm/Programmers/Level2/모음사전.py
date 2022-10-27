def solution(word):
    answer = 0

    def dfs(L, S):
        tmp.append(S)
        if S == word:
            return
        if L == 5:
            return
        else:
            for i in range(5):
                dfs(L + 1, S + words[i])

    words = ['A', 'E', 'I', 'O', 'U']
    tmp = []
    dfs(0, '')
    answer = tmp.index(word)
    return answer