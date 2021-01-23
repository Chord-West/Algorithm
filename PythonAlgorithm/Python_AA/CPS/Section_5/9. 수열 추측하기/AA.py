import sys
#sys.stdin = open("input.txt","rt")

def DFS(L):
    global m
    if L==n:
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]*b[i]
        if sum==m:
            print(" ".join(map(str,arr)))
            sys.exit(0)



    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                arr[L] = i
                DFS(L+1)
                ch[i]=0

if __name__ == "__main__":
    n,m = map(int,input().split())
    ch=[0]*(n+1)
    arr=[0]*n
    b=[1]*n
    for i in range(1,n):
        b[i]=(b[i-1]*(n-i)//i) # 조합
    DFS(0)