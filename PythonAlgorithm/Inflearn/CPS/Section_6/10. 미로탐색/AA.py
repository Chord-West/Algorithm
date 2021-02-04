import sys
# sys.stdin = open("input.txt","rt")
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<=6 and 0<=ny<=6 and maze[ny][nx]==0:
                maze[ny][nx]=1
                dfs(nx,ny)
                maze[ny][nx]=0

if __name__ == "__main__":
    maze = [list(map(int,input().split())) for _ in range(7)]
    maze[0][0]=1
    cnt=0
    dfs(0,0)
    print(cnt)