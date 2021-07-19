import sys
sys.stdin = open("input.txt","rt")
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board=[]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

ry,rx,by,bx=0,0,0,0
for i in range(N):
    tmp=[]
    for j,x in enumerate(input().rstrip()):
        tmp.append(x)
        if x=='R':
            ry,rx=i,j
        elif x=='B':
            by,bx=i,j
    board.append(tmp)
Q = deque([(ry,rx,by,bx,0)])
visited[ry][rx][by][bx] = True
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def move(y,x,dy,dx):
    count=0
    while board[y+dy][x+dx]!='#' and board[y+dy][x+dx]!='O':
        y+=dy
        x+=dx
        count+=1
    return y,x,count


while Q:
    ry,rx,by,bx,cnt=Q.popleft()
    if cnt>10:
        break

    for i in range(4):
        next_ry,next_rx , r_count = move(ry,rx,dy[i],dx[i]) # RED
        next_by, next_bx, b_count = move(by, bx, dy[i], dx[i])  # BLue
        if board[next_by][next_bx] == 'O':
            continue
        if board[next_ry][next_rx] == 'O':
            print(cnt)
        if next_ry == next_by and next_rx == next_bx:
            if r_count>b_count:
                next_ry -=dy[i]
                next_rx -= dx[i]
            else:
                next_by -= dy[i]
                next_bx -= dx[i]

        if not visited[next_ry][next_rx][next_by][next_bx]:
            visited[next_ry][next_rx][next_by][next_bx] = True
            Q.append((next_ry, next_rx, next_by, next_bx, cnt + 1))
print(-1)
