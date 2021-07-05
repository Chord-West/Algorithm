import sys
from collections import deque
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
n = int(input())
tree =[[] for _ in range(n+1)]

for _ in range(n):
    tmp = list(map(int,input().split()))[:-1]
    v = tmp.pop(0)
    while tmp:
        tree[v].append((tmp.pop(0),tmp.pop(0)))

def bfs(start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start]=0
    _max = [0,0]
    while q:
        now = q.popleft()
        for next, w in tree[now]:
            if visited[next]==-1:
                visited[next] = visited[now]+w
                q.append(next)
                if _max[0] < visited[next]:
                    _max = visited[next],next
    return _max

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)

