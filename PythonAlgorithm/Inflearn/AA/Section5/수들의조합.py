import sys
sys.stdin = open("input.txt","rt")

def DFS(L):
    global cnt
    if L==k:
        if sum(res)%m==0:
            cnt+=1
    else:
        for i in range(len(num)):
            if ch[i]==0 and res[L-1]<num[i]:
                ch[i]=1
                res[L]=num[i]
                DFS(L+1)
                ch[i]=0

if __name__ =="__main__":
    n,k= map(int,input().split())
    num=list(map(int,input().split()))
    ch=[0]*n
    cnt=0
    m=int(input())
    res = [0] * m
    DFS(0)
    print(cnt)