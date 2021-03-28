import sys

sys.stdin = open("input.txt","rt")

board= [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
board= sorted(board,key=lambda x:(x[0],x[1]))
for x,y in board:
    print("%d %d"%(x,y))