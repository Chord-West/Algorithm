import sys
#sys.stdin=open("input.txt","rt")

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    global cnt
    for i in range(4):
        nx = x+dx[i]
        ny= y+dy[i]
        if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and board[nx][ny]==1:
            ch[nx][ny]=1
            cnt+=1
            dfs(nx,ny)

if __name__ =="__main__":
    n = int(input())
    board = [[int(x)for x in input()] for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    cnt=0
    ans=0
    li=[]
    for i in range(n):
        for j in range(n):
            cnt=0
            dfs(i,j)
            if cnt!=0:
                ans+=1
                li.append(cnt)
    print(ans)
    li.sort()
    for x in li:
        print(x)