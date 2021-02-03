import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    maze = [list(map(int,input().split())) for _ in range(7)]
    #    D,Up, R, L
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    maze[0][0]=2

    Q = deque()
    Q.append((0,0))
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > 6 or ny > 6:
                continue
            elif maze[ny][nx]==0:
                maze[ny][nx]=maze[y][x]+1
                Q.append((nx,ny))
    if maze[6][6]==0:
        print(-1)
    else:
        print(maze[6][6]-2)






