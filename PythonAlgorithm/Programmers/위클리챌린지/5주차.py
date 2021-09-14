from itertools import permutations

def solution(word):
    def dfs(L,S,cnt):
        tmp.append(S)
        if S==word:
            return answer
        if L==n:
            return
        else:
            for i in range(n):
                dfs(L+1,S+words[i],cnt+1)
    answer = 0
    words = ['A','E','I','O','U']
    n = len(words)
    tmp=[]
    dfs(0,'',0)
    answer = tmp.index(word)
    return answer