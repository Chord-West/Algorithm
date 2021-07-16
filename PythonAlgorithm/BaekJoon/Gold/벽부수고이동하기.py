import sys
from collections import deque
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

def bfs(sx,sy):
    visited[sy][sx][0]=1
    q = deque([(sx,sy,0)])
    while q:
        x,y,z=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if Map[ny][nx]==0 and visited[ny][nx][z]==-1:
                    visited[ny][nx][z] = visited[y][x][z]+1
                    q.append((nx,ny,z))
                elif Map[ny][nx] == 1 and z==0 and visited[ny][nx][1] == -1:
                    visited[ny][nx][1] = visited[y][x][z] + 1
                    q.append((nx, ny,1))




N,M = map(int,input().split())
Map=[]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# 방문 테이블, 0은 벽 안부숨, 1 벽 부숨
visited =[[[-1]*2 for _ in range(M)] for _ in range(N)]


for _ in range(N):
    Map.append([int(i) for i in  input().rstrip('\n')])

bfs(0,0)
ans1 = visited[N-1][M-1][0]
ans2 = visited[N-1][M-1][1]
if ans1==-1 and ans2!=-1:
    print(ans2)
elif ans1!=-1 and ans2==-1:
    print(ans1)
else:
    print(min(ans1,ans2))