def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [0 for x in words]
    def dfs(begin):
        nonlocal answer
        stacks = [begin]

        while stacks:
            stack = stacks.pop()
            if stack == target:
                return

            for i in range(len(words)):
                if len([j for j in range(len(words[i])) if words[i][j]!=stack[j]]) ==1:
                    if visited[i]!=0:
                        continue
                    visited[i] = 1

                    stacks.append(words[i])

            answer+=1

    dfs(begin)
    return answer



begin ="hit"
target="cog"
words=["hot","dot","dog","lot","log","cog"]

print(solution(begin, target, words))