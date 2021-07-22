import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline


dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]
N,M,x,y,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
command = list(map(int,input().split()))
dice = [0 for _ in range(7)]
for c in command:

    if 0<=x+dx[c]<M and 0<=y+dy[c]<N:
        x += dx[c]
        y += dy[c]
        if c == 1:
            dice[6],dice[3],dice[1],dice[4]=dice[3],dice[1],dice[4],dice[6]
        elif c == 2:
            dice[6],dice[4],dice[3],dice[1]=dice[4],dice[1],dice[6],dice[3]
        elif c == 3:
            dice[6],dice[5],dice[1],dice[2]=dice[5],dice[1],dice[2],dice[6]
        elif c == 4:
            dice[6], dice[2], dice[1], dice[5] = dice[2], dice[1], dice[5], dice[6]
        if board[y][x]==0:
            board[y][x]=dice[6]
        else:
            dice[6]=board[y][x]
            board[y][x]=0

        print(dice[1])

