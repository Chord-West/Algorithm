import sys
#sys.stdin = open("input.txt","rt")

def DFS(L,sum):
    global total
    if L==k:
        if 0<sum<=total:
            ch[sum]=1
    else:
        DFS(L+1,sum+w[L])
        DFS(L+1, sum)
        DFS(L+1, sum-w[L])


if __name__ == "__main__":
    k= int(input())
    w = list(map(int,input().split()))
    total=sum(w)
    ch=[0]*(total+1)
    DFS(0,0)
    cnt=0
    for i in range(1,len(ch)):
        if ch[i]==0:
            cnt+=1
    print(cnt)