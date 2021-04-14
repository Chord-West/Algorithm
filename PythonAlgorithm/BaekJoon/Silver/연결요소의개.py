import sys
sys.stdin = open("input.txt","rt")
sys.setrecursionlimit(10000000)
r = sys.stdin.readline

def dfs(v):
    for x in graph[v]:
        if ch[x]==0:
            ch[x]=1
            dfs(x)

n,m = map(int,r().split())
ch = [0]*(n+1)
graph = [[] for _ in range(n+1)]


for _ in range(m):
    x,y = map(int,r().split())
    graph[x].append(y)
    graph[y].append(x)
answer=0
print(graph)
for i in range(1,n+1):
    if ch[i]==0:
        answer+=1
        dfs(i)

