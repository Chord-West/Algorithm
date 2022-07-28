from collections import deque


def solution(rows, columns, queries):
    answer = []
    board = [[j + i * columns for j in range(1, columns + 1)] for i in range(rows)]
    for y1, x1, y2, x2 in queries:
        position = []
        q = deque([])
        for i in range(x1 - 1, x2):
            position.append([y1 - 1, i])
            q.append(board[y1 - 1][i])
        for j in range(y1, y2):
            position.append([j, x2 - 1])
            q.append(board[j][x2 - 1])
        for k in range(x2 - 2, x1 - 2, -1):
            position.append([y2 - 1, k])
            q.append(board[y2 - 1][k])
        for l in range(y2 - 2, y1 - 1, -1):
            position.append([l, x1 - 1])
            q.append(board[l][x1 - 1])
        q.appendleft(q.pop())
        answer.append(min(q))
        for idx, pos in enumerate(position):
            board[pos[0]][pos[1]] = q[idx]

    return answer