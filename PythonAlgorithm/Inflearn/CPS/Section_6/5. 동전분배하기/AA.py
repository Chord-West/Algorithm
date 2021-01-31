import sys
#sys.stdin = open("input.txt","rt")

def dfs(L):
    global ans
    if L == n:
        cha=max(p)-min(p)
        if cha<ans:
            tmp=set()
            for x in p:
                tmp.add(x)
            if len(tmp)==3:
                ans=cha
    else:
        for i in range(3):
            p[i]+=coins[L]
            dfs(L+1)
            p[i]-=coins[L]

if __name__ == "__main__":
    n = int(input())
    coins = [int(input()) for _ in range(n)]
    p=[0]*3
    ans=2147000
    dfs(0)
    print(ans)