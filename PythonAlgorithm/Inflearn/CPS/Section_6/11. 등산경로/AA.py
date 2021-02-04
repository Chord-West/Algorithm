import sys
#sys.stdin = open("input.txt","rt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global cnt
    if x==max_x and y==max_y:
        cnt+=1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and bmap[x][y]<bmap[nx][ny] and ch[nx][ny]==0:
                ch[nx][ny]=1
                dfs(nx,ny)
                ch[nx][ny]=0


if __name__ == "__main__":
    n = int(input())
    bmap=[list(map(int,input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max=-1
    max_x,max_y=0,0
    min=99999
    min_x, min_y = 0, 0
    cnt=0
    for i in range(n):
        for j in range(n):
            if bmap[i][j]<min:
                min =bmap[i][j]
                min_x,min_y=i,j
            if bmap[i][j]>max:
                max= bmap[i][j]
                max_x,max_y=i,j
    ch[min_x][min_y]=1
    dfs(min_x,min_y)
    print(cnt)