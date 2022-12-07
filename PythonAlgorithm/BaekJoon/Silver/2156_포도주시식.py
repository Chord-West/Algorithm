import sys

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())

zan = [0] + [int(sys.stdin.readline()) for _ in range(n)] + [0]
dp = [0] * (n+2)
print(zan)
dp[1] = zan[1]
dp[2] = dp[1] + zan[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-3]+zan[i-1]+zan[i], dp[i-2]+zan[i], dp[i-1])
print(dp[n])