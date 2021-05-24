from collections import deque
def solution(maps):
    n = len(maps[0])
    m = len(maps)
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    q = deque([[0,0]])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[ny][nx]==1:
                maps[ny][nx] = maps[y][x]+1
                q.append([nx,ny])
    if maps[m-1][n-1]==1:
        return -1
    else:
        return maps[m-1][n-1]