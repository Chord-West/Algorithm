#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
board = list(map(int,input().split()))
m = int(input())

board.sort(reverse=True)

for _ in range(m):
    idx=0
    idx2=n-1
    while board[idx] == board[idx+1]:
        idx+=1
    board[idx]-=1
    while board[idx2] == board[idx2-1]:
        idx2-=1
    board[idx2]+=1

print(board[0]-board[n-1])