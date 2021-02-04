import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

def dfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<n and 0<=ny<n and smap[nx][ny]==1 and ch[nx][ny]==0:
                ch[nx][ny]=1
                q.append((nx,ny))

if __name__ == "__main__":
    n = int(input())
    smap = [list(map(int,input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if ch[i][j]==0 and smap[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)

