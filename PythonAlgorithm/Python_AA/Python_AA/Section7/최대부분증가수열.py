import sys
sys.stdin=open("input.txt","rt")

n = int(input())
arr = list(map(int,input().split()))
max=0
for i in range(n):
    dp=[]
    dp.append(arr[i])
    idx=0
    for j in range(i+1,n):
        if arr[j]>dp[idx]:
            dp.append(arr[j])
            idx+=1
    if max<len(dp):
        max=len(dp)
    dp.clear()

print(max)
