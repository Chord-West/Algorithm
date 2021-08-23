from collections import deque


def solution(m, n, board):
    answer = 0
    board = [list(map(str, b)) for b in board]

    def resort():
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] != 0:
                    x, y = j, i
                    while y + 1 < m and board[y + 1][x] == 0:
                        board[y + 1][x], board[y][x] = board[y][x], board[y + 1][x]
                        y += 1

    def find(x, y):
        target = board[y][x]
        if target == board[y][x + 1] and target == board[y + 1][x] and target == board[y + 1][x + 1]:
            q.append((x, y))
            q.append((x + 1, y))
            q.append((x, y + 1))
            q.append((x + 1, y + 1))
            return
        else:
            return

    while True:
        tmp = set([])
        q = deque([])
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0:
                    find(j, i)
        if not q:
            break
        while q:
            x, y = q.popleft()
            if board[y][x] != 0:
                board[y][x] = 0
                tmp.add((x, y))
        resort()
        answer += len(tmp)
    return answer