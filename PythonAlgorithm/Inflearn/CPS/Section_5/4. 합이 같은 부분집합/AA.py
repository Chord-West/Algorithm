import sys
#sys.stdin = open("input.txt","rt")

def DFS(v):
    if v==n+1:
        sum=0
        sum2=0
        for i in range(1,n+1):
            if ch[i]==1:
                sum+=num[i]
            else:
              sum2+=num[i]
        if sum==sum2:
            print("YES")
            sys.exit(0)
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__ == "__main__":
    n=int(input())
    num = list(map(int,input().split()))
    num.insert(0,0)
    p=dict()
    ch=[0]*(n+1)
    DFS(1)
    print("NO")