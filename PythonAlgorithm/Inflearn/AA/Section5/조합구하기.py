import sys
#sys.stdin = open("input.txt","rt")

def DFS(L):
    global cnt
    if L==m:
        for x in arr:
            if x!=0:
                print(x, end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0 and arr[L-1]<i:
                arr[L]=i
                ch[i]=1
                DFS(L+1)
                ch[i]=0

if __name__ =="__main__":
    n,m = map(int,input().split())
    ch=[0]*(n+1)
    arr=[0]*(m+1)
    cnt=0
    DFS(0)
    print(cnt)
