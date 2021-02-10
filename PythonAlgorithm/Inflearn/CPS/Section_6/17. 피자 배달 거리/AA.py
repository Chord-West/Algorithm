import sys
#sys.stdin = open("input.txt","rt")

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,sum):
    global cnt, min
    if cnt==4:
        if min>sum:
            min=sum-1
    else:
        for i in range(4):
            nx= x + dx[i]
            ny= y + dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0:
                ch[nx][ny]=1
                if city[nx][ny]==2:
                    cnt+=1
                    dfs(nx,ny,sum+abs(sx-nx)+abs(sy-ny))
                    cnt-=1
                else:
                    dfs(nx,ny,sum)

if __name__ == "__main__":
    n,m = map(int, input().split())
    city = [list(map(int,input().split())) for _ in range(n)]
    min,cnt = 999999,0
    sx,sy = 0,0
    for i in range(n):
        for j in range(n):
            if city[i][j]==1:
                ch = [[0]*n for _ in range(n)]
                sx,sy=i,j
                ch[i][j]=1
                dfs(i,j,0)
    print(min)