import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
# d가 0 : 북쪽 , 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
ans=0
dx = [0,1,0,-1]
dy = [-1,0,1,0]


N,M = map(int,input().split())
def move(x,y,d):
    global ans
    if board[y][x]==0:
        board[y][x]=2
        ans+=1
    for _ in range(4):
        nd = (d-1)%4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if board[ny][nx] == 0:
            move(nx,ny,nd)
            return
        d = nd
    nd = (d+2)%4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if board[ny][nx]==1:
        return
    move(nx,ny,d)

# 현재 방향에서 왼쪽으로
ry,rx,rd = map(int,input().split())
# 0은 빈칸 1은 벽
board =[list(map(int,input().split())) for _ in range(N)]
move(rx,ry,rd)
print(ans)
