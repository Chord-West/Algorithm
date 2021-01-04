import sys
sys.stdin=open("input.txt","rt")

n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0) # 1부터 진행하기 위해
ans=0
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1): # 뒤로 가면서 확인
        if arr[i]>arr[j] and dp[j]>max:
            max=dp[j]
    dp[i]=max+1
    if dp[i]>ans:
        ans=dp[i]

print(ans)
