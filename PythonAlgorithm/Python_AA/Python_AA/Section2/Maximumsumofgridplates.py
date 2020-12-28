#import sys

# sys.stdin = open("input.txt","rt")

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
answer=[]

cross = 0
rcross = 0
for i in range(n):
    row = 0
    col = 0

    for j in range(n):
        row+=board[i][j]
        col+=board[j][i]
    answer.append(row)
    answer.append(col)
    cross+=board[i][i]
    rcross+=board[n-1-i][n-1-i]
answer.append(cross)
answer.append(rcross)

answer.sort(reverse=True)
print(answer[0])