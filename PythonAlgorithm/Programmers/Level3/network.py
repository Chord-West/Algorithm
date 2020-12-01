
def solution(n,computers):
    answer =0
    visited=[0]*n # 초기화
    net = [ [j for j in range(n) if computers[i][j]==1] for i in range(n)]
    def dfs(start):
        visited[start]=1
        for x in net[start]:
            if visited[x]==0:
                dfs(x)

    for i in range(n):
        if visited[i]==0:
            dfs(i)
            answer+=1


    return answer


n=3
computers=[[1,1,0],[1,1,0],[0,0,1]]

print(solution(n,computers))