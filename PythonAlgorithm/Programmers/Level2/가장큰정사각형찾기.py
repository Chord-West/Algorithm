def solution(board):
    max_point = 0
    for i in range(len(board)):
        max_point+=sum(board[i][:])
    if max_point ==0:
        return 0
    max_point = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]==0:
                continue
            else:
                min_point = min(board[i][j-1],board[i-1][j],board[i-1][j-1])
                min_point+=1
                board[i][j] = min_point
                if max_point < board[i][j]:
                    max_point = board[i][j]
    if max_point==0:
        return 1
    return max_point**2