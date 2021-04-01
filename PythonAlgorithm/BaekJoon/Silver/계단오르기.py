import sys
sys.stdin = open("input.txt","rt")

n = int(input())

dp=[ int(input()) for _ in range(n)]
dp.insert(0,0)

cnt=1
for i in range(2,n+1):
    if cnt==2:
        dp[i] = dp[i] + dp[i-2]
        cnt=1
    else:
        dp[i] = max(dp[i]+dp[i-2],dp[i]+dp[i-1])
        cnt+=1
print(dp[-1])