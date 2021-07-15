import sys
from collections import deque
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

def bfs(sx,sy):
    Map[sy][sx]=1
    q = deque([(sx,sy)])
    ch_one=False
    ch_firt=False
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if Map[ny][nx]==1:
                    if not ch_one:
                        Map[ny][nx]=Map[y][x]+1
                        q.append((nx,ny))
                        ch_firt=True
                elif Map[ny][nx]==0:
                    Map[ny][nx] = Map[y][x] + 1
                    q.append((nx, ny))
        if ch_firt:
            ch_one=True



N,M = map(int,input().split())
Map=[]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(N):
    Map.append([int(i) for i in  input().rstrip('\n')])

bfs(0,0)
print(Map[N-1][M-1])