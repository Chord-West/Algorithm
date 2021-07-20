from collections import deque
import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

def rotate(d,c):
    if c=='L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

N = int(input()) # 보드의 크키 N*N
K = int(input()) # 사과의 개수
game_map = [['0']*(N+1) for _ in range(N+1)]
for _ in range(K):
    a,b = map(int,input().split()) # 사과의 위치
    game_map[a][b]='A'
game_map[1][1]='Z'

dx = [1,0,-1,0]
dy = [0,1,0,-1]

times={}
L = int(input()) # 뱀의 방향변한 횟수
for _ in range(L):
    a,c = input().split()
    times[int(a)]=c # x, c : L 왼쪽 90도 , D 오른쪽 90도
snake =deque([(1,1)]) # 뱀 초기위치
direction = 0
time=1
x,y=1,1
while True:
    x,y = x + dx[direction], y + dy[direction]
    if 0<x<=N and 0<y<=N and game_map[y][x]!='Z':
        if game_map[y][x]!='A': # 사과가 아닌 경우
            tmp_x,tmp_y = snake.popleft()
            game_map[tmp_y][tmp_x] = '0' # 꼬리제거
        game_map[y][x]='Z'
        snake.append((x,y))
        if time in times:
            direction = rotate(direction,times[time])
        time+=1
    else:
        print(time)
        break





