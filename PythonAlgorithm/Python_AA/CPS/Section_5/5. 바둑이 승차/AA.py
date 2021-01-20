import sys
#sys.stdin = open("input.txt","rt")

def DFS(idx,sum):
    if sum>c:
        return
    if idx==n:
        global max
        if sum>max:
            max=sum
    else:
        DFS(idx + 1, sum + w[idx])
        DFS(idx + 1, sum)

if __name__ == "__main__":
    c,n = map(int, input().split())
    w = [int(input()) for _ in range(n)]
    max=0
    w.sort()
    DFS(0,0)
    print(max)