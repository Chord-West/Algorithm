import sys
sys.stdin = open("input.txt")

n=int(input())
arr=list(map(int,input().split()))

dp=[0]*(n+1)
arr.insert(0,0)
dp[1]=1
ans=0

for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        if arr[i]>arr[j] and dp[j]>max:
            max=dp[j]
    dp[i]=max+1
    if dp[i]>ans:
        ans=dp[i]

print(ans)