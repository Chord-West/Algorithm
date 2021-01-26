#import sys
#sys.stdin = open("input.txt","rt")

board = [list(map(int,input().split())) for _ in range(9)]

def sudoku(board):
# 열, 행 검사
    for i in range(9):
        row=[0]*10
        col=[0]*10
        for j in range(9):
            row[board[i][j]]+=1
            col[board[j][i]] += 1
            if row[board[i][j]] >1 or col[board[i][j]] >1 :
                return False
    for i in range(3):
        for j in range(3):
            tmp = [0] * 10
            for r in range(3 * i, 3 * i + 3):
                for c in range(3 * i, 3 * i + 3):
                    tmp[board[r][c]] += 1
                    if tmp[board[r][c]] > 1:
                        return False
    return True

if not sudoku(board):
    print("NO")
else :
    print("YES")