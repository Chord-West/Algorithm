import sys
from itertools import combinations
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline



N,K = map(int,input().split())
coins=[]
for _ in range(N):
    coins.append(int(input()))
ans = 0

count=[0]*N
div_coin = [K//coin for coin in coins]

visited=[0]*N
def dfs(S):
    global ans,count
    if S > K:
        return
    if S == K:
        for i in range(len(count)):
            if count[i]==div_coin[i]:
                visited[i]=1
        ans += 1
        return
    else:
        for i in range(len(coins)):
            if visited[i] == 0:
                count[i] += 1
                dfs(S + coins[i])
                count[i]-=1
dfs(0)

print(ans)