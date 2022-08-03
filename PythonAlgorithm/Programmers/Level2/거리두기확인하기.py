from collections import deque
import copy


def solution(places):
    answer = []
    for place in places:
        board = [list(map(str, x)) for x in place]
        q = deque(findP(board))  # y,x
        if validate(board, q):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def findP(board):
    tmp = []
    for y, v in enumerate(board):
        for x, k in enumerate(v):
            if k == 'P':
                tmp.append([y, x])
    return tmp


def validate(board, q):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    tmp = copy.copy(q)
    while q:
        y, x = q.popleft()
        if board[y][x] == 'P':
            board[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if board[ny][nx] == 'O':
                    board[ny][nx] = board[y][x] + 1
                    q.append([ny, nx])
                if board[y][x] == 1 and board[ny][nx] == 2:
                    return False

    print(board)
    return True