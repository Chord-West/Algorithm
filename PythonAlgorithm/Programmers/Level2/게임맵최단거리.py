from collections import deque
def solution(maps):
    ys, xs = len(maps), len(maps[0])
    ch = [[0] * xs for i in range(ys)]
    q = deque([[0, 0]])
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    ch[0][0] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < xs and 0 <= ny < ys:
                if ch[ny][nx] == 0 and maps[ny][nx] == 1:
                    ch[ny][nx] = ch[y][x] + 1
                    q.append([ny, nx])

    return -1 if ch[ys - 1][xs - 1] == 0 else ch[ys - 1][xs - 1]