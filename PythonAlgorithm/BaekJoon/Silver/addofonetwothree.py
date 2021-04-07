import sys
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline


def dfs(L,sum):
    global cnt
    if sum >L:
        return
    if sum==L:
        cnt+=1
    else:
        for i in range(1,4):
            dfs(L,sum+i)

cnt=0
for _ in range(int(r())):
    L=int(r())
    cnt=0
    dfs(L,0)
    print(cnt)

