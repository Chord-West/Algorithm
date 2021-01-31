import sys
#sys.stdin = open("input.txt","rt")

def dfs(L,sum):
    global cnt
    if sum>t:
        return
    if L==k:
        if sum==t:
            cnt+=1
    else:
        for i in range(n[L]+1):
            dfs(L+1,sum+(p[L]*i))

if __name__ == "__main__":
    t = int(input())
    k = int(input())
    p,n=[],[]
    for _ in range(k):
        a,b = map(int,input().split())
        p.append(a)
        n.append(b)
    cnt=0
    dfs(0,0)
    print(cnt)