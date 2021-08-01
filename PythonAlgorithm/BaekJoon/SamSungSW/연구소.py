import sys
import copy
from collections import deque
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
def spread_virus():
    global max_value
    copy_board = copy.deepcopy(board)
    q = deque([])
    for i in range(N):
        for j in range(M):
            if copy_board[i][j]==2:
                q.append((j,i))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if copy_board[ny][nx]==0:
                    copy_board[ny][nx]=2
                    q.append((nx,ny))
    cnt = sum(c.count(0) for c in copy_board)
    max_value = max(cnt,max_value)
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
max_value = 0

# 벽 선택하기
q = deque([])
def wall(count):
    if count==3:
        spread_virus()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(count+1)
                board[i][j] = 0

wall(0)
print(max_value)