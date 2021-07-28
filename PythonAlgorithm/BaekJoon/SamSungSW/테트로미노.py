import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def find(x,y):
    global ans
    for i in range(19):
        tmp=0
        for dx,dy in tetrimino[i]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N:
                tmp+=board[ny][nx]
            else:
                break
        ans = max(ans,tmp)


N,M = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
ans = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
tetrimino =[
    [(0,0),(1,0),(2,0),(3,0)], # ㅡ
    [(0,0),(0,1),(0,2),(0,3)], # ㅣ
   # ㅁ 자
    [(0,0),(0,1),(1,1),(1,0)],
   # L 자
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    # ㅗ 자
    [(0, 0), (0, 1), (1, 1), (0, 2)],
    [(1, 0), (1, 1), (0, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 1)],
    # ㄹ 자
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
]


for i in range(N):
    for j in range(M):
        find(j,i)
print(ans)