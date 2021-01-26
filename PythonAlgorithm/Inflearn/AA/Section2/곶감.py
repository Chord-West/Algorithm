#import sys

#sys.stdin = open("input.txt","rt")
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    row , mv, count = map(int,input().split())
    if mv==0:
        for _ in range(count):
            board[row-1].append(board[row-1].pop(0))
    else:
        for _ in range(count):
            board[row - 1].insert(0,board[row - 1].pop())

sum=0
s,e=0,n
for i in range(n):
    for j in range(s,e):
       sum+=board[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(sum)