import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0:
                ch[nx][ny]=1
                q.append((nx,ny))

if __name__ == "__main__":
    n = int(input())
    smap = [list(map(int,input().split())) for _ in range(n)]
    max = -1
    min = 101
    cnt = 0
    ans = 0
    for x in smap:
        for y in x:
            if max<y:
                max=y
            if min>y:
                min=y

    for x in range(min,max+1):
        ch = [[0] * n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if smap[i][j]<=x:
                    ch[i][j]=1
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0:
                    cnt+=1
                    bfs(i,j)
        if ans<cnt:
            ans=cnt

    print(ans)
