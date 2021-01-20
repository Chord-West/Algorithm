import sys
sys.stdin = open("input.txt","rt")

def DFS(idx,sum,tsum):
    global max
    if sum+(total-tsum)<max:
        return
    if sum>c:
        return
    if idx==n:

        if sum>max:
            max=sum
    else:
        DFS(idx + 1, sum + w[idx],tsum+w[idx])
        DFS(idx + 1, sum,tsum+w[idx])

if __name__ == "__main__":
    c,n = map(int, input().split())
    w = [int(input()) for _ in range(n)]
    max=0
    total=sum(w)
    w.sort()
    DFS(0,0,0)
    print(max)