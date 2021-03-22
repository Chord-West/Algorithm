def solution(m, n, board):
    def check(y, x):
        init = board[y][x]
        cnt = 0
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if init == board[ny][nx]:
                cnt += 1
        if cnt == 3:
            block[y][x] = 1
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                block[ny][nx] = 1

    answer = 0
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    board = [list(map(str, x)) for x in board]
    block = [[0] * n for _ in range(m)]
    for i in range(m - 1):
        for j in range(n - 1):
            check(i, j)
    # print(block)
    for i in range(m):
        for j in range(n):
            if block[i][j] == 1:
                board[i][j] = 0
    for x in zip(board):
        print(x)

    return answer