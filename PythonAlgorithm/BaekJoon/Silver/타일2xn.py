import sys
r= sys.stdin.readline

n = int(r())
dp=[0]*(1001)

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp)