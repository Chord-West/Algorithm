import sys
from collections import deque

def bfs(v):
    count = 0
    q = deque([[v,count]])
    while q:
        arr = q.popleft()
        x = arr[0]
        count = arr[1]
        if not visited[x]:
            visited[x] = True
            userCount[x] += count
            count+=1
            for v in user[x]:
                q.append([v,count])

sys.stdin = open("input.txt","rt")
r = sys.stdin.readline
n,m = map(int,r().split())
user=[[] for _ in range(n+1)]
userCount = [0]*(n+1)


for i in range(m):
    a,b = map(int,r().split())
    user[a].append(b)
    user[b].append(a)

for start in range(1,n+1):
    visited = [False]*(n+1)
    bfs(start)

print(userCount.index(min(userCount[1:])))