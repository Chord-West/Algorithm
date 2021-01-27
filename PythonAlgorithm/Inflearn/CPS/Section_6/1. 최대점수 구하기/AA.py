import sys
#sys.stdin = open("input.txt","rt")

def DFS(L,time,sum):
    global max
    if time>m:
        return
    if L==n:
        if sum>max:
            max=sum
    else:
       DFS(L+1,time+arr[L][1],sum+arr[L][0])
       DFS(L + 1, time, sum )

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    max=0
    DFS(0,0,0)
    print(max)