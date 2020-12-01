from collections import deque
import sys

sys.stdin = open("input.txt","rt")

n, m ,v = map(int, input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    x.sort()

print(graph)

visited = [False]*(n+1)

def BFS(graph,v,visited):
    visited[v]=True
    queue = deque([v])
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def DFS(graph,v,visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)


DFS(graph,v,visited)
print()
visited = [False]*(n+1)
BFS(graph,v,visited)