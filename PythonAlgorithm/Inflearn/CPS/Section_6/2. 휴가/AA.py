import sys
#sys.stdin = open("input.txt","rt")

def DFS(T,P):
    global max
    if T>n:
        return
    if T==n:
        if P>max:
            max=P
    else:
        DFS(T + arr[T][0],P+arr[T][1])
        DFS(T+1,P)

if __name__ == "__main__":
    n = int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    max=0
    DFS(0,0)
    print(max)