import sys
from collections import deque
sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    maze = [list(map(int,input().split())) for _ in range(7)]
    dis=[[0]*7 for _ in range(7)]
    #    D,Up, R, L
    dx = [-1,0,1,-0]
    dy = [0,-1,0,1]
    maze[0][0]=1

    Q = deque()
    Q.append((0,0))
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=6 and 0<=ny<=6 and maze[ny][nx]==0:
                maze[ny][nx]=1
                dis[ny][nx]=dis[y][x]+1
                Q.append((nx,ny))
    if dis[6][6]==0:
        print(-1)
    else:
        print(dis[6][6])






