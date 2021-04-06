import sys
from collections import deque
sys.stdin = open("input.txt","rt")

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 1
n,m = map(int,input().split())
tomatos = [list(map(int,input().split())) for _ in range(m)]
location = []
zero=0
for i in range(m):
    for j in range(n):
        if tomatos[i][j]==1:
            location.append((j,i))

q = deque(location)
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if tomatos[ny][nx] ==0:
                tomatos[ny][nx] = tomatos[y][x]+1
                answer = tomatos[ny][nx]
                q.append((nx,ny))
for i in range(m):
    for j in range(n):
        if tomatos[i][j] ==0:
            answer=-1
            break
if answer ==-1:
    print(answer)
else:
    print(answer-1)
