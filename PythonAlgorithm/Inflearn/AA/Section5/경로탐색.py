import sys
#sys.stdin = open("input.txt","rt")

def DFS(v):
    global cnt
    if v==n:
        cnt+=1
    else:
        for i in range(1,n+1):
            if gp[v][i]==1 and ch[i]==0: # 방문을 한번도 안했고, 갈 수 있으면 DFS로 탐색
                ch[i]=1
                DFS(i)
                ch[i]=0


if __name__ == "__main__":
    n,m = map(int,input().split())
    ch=[0]*(n+1)
    gp=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x,y=map(int,input().split())
        gp[x][y]=1

    cnt=0
    ch[1]=1
    DFS(1)
    print(cnt)
