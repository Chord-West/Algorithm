import sys
#sys.stdin = open("input.txt","rt")

dx = [-1,1,0]
dy = [0,0,-1]

def dfs(x,y):
    if y==0:
        print(x)
        sys.exit()
    else:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<10 and 0<=ny<10 and ch[ny][nx]==0 and ladder[ny][nx]==1:
                ch[ny][nx]=1
                dfs(nx,ny)


if __name__ == "__main__":
    ladder = [ list(map(int,input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for i in range(10):
        if ladder[9][i]==2:
            dfs(i,9)

