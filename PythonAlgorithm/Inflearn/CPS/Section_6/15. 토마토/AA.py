import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    m,n = map(int,input().split()) # 6 4
    tomato = [list(map(int,input().split())) for _ in range(n)]
    dis = [[0]*m for _ in range(n)]
    cnt=0
    Q = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(m):
            if tomato[i][j]==1:
                Q.append((i,j))
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if cnt == 0:
                if 0<=nx<n and 0<=ny<m and tomato[nx][ny]==0:
                    tomato[nx][ny] = 1
                    dis[nx][ny] = dis[x][y]+1
                    Q.append((nx,ny))
    flag = 1
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                flag = 0
    result=0
    if flag==1:
        for i in range(n):
            for j in range(m):
                result = max(result,dis[i][j])
        print(result)
    else:
        print(-1)
