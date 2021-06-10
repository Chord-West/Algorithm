import sys
from collections import deque
sys.stdin = open("input.txt","rt")
n , m = map(int,input().split())
maze = [[int(i) for i in input()] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y):
    q = deque([[x,y]])
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<m and 0<=ny<n and maze[ny][nx]==1 :
                maze[ny][nx] = maze[b][a] + 1
                q.append([nx,ny])


dfs(0,0)
print(maze[n-1][m-1])
