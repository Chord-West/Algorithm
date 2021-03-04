import sys

sys.stdin = open("input.txt","rt")

n = int(input())
foods = list(map(int,input().split()))
# a
dp = [0] * n

# 다이나믹 프로그래밍 진행 ( 보텀업 )
dp[0] = foods[0]
dp[1] = max(foods[0],foods[1])
for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+foods[i])

print(dp[n-1])
