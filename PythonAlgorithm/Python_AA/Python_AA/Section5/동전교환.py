import sys
#sys.stdin = open("input.txt","rt")

def DFS(idx,sum):
    global min
    if idx>min:
        return
    if sum>m:
        return
    if sum==m:
        if idx<min:
            min=idx
    for i in range(len(coins)):
        DFS(idx+1,sum+coins[i])

if __name__ == "__main__":
    n = int(input())
    coins = list(map(int,input().split()))
    coins.sort(reverse=True)
    m = int(input())
    total= sum(coins)
    cr = total // coins[n - 1]
    min=99999
    DFS(0,0)
    print(min)
