import sys
sys.stdin = open("input.txt","rt")

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(L,s):
    global ans
    if L==m:
        sum = 0
        for j in range(len(hs)):
            x1=hs[j][0]
            y1=hs[j][1]
            dis = 21470000
            for x in cb:
                x2=pz[x][0]
                y2=pz[x][1]
                dis= min(dis,abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<ans:
            ans=sum
    else:
        for i in range(s,len(pz)):
            cb[L]=i
            dfs(L+1,i+1)

if __name__ == "__main__":
    n,m = map(int, input().split())
    city = [list(map(int,input().split())) for _ in range(n)]
    hs=[]
    pz=[]
    cb = [0] * m
    ans = 999999
    cnt=0
    for i in range(n):
        for j in range(n):
            if city[i][j]==1:
                hs.append((i,j))
            elif city[i][j]==2:
                pz.append((i,j))
    dfs(0,0)
    print(ans)