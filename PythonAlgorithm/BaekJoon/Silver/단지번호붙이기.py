import sys
from collections import deque
sys.stdin = open("input.txt","rt")
n = int(input())
arr = [[int(i) for i in input()]for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited=[[0]*n for _ in range(n)]
ans =[]
def bfs(a,b):
    q = deque([[a,b]]) #(y,x)
    cnt=0
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[ny][nx] ==1 and visited[ny][nx]==0:
                    visited[ny][nx]=1
                    cnt+=1
                    q.append([ny,nx])

    ans.append(cnt)
for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and visited[i][j]==0:
            bfs(i,j)
ans.sort()
print(len(ans))
for a in ans:
    print(a)