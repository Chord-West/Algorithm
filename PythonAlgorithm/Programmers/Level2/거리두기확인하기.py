from collections import deque
import copy


def solution(places):
    answer = []
    for place in places:
        board = [list(map(str, x)) for x in place]
        start = findP(board)
        answer.append(validate(start, board))

    return answer


def findP(board):
    tmp = []
    for y, v in enumerate(board):
        for x, k in enumerate(v):
            if k == 'P':
                tmp.append([y, x])
    return tmp


def validate(start, board):
    for s in start:
        q = deque([s])  # y,x
        visited = [[0] * 5 for i in range(5)]
        distance = [[0] * 5 for i in range(5)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        visited[q[0][0]][q[0][1]] = 1
        while q:
            y, x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    if board[ny][nx] == 'O':
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                        q.append([ny, nx])
                    if board[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0

    return 1