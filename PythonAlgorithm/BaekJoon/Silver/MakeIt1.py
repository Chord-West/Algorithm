import sys

n=int(sys.stdin.readline())

dp =[0,0,1,1] # 0,1,2,3


for x in range(4,n+1):
    dp.append(dp[x-1]+1)
    if x%2==0:
        dp[x]=min(dp[x//2],dp[x-1])+1
    if x%3==0:
        dp[x] = min(dp[x // 3], dp[x - 1]) + 1
print(dp[n])