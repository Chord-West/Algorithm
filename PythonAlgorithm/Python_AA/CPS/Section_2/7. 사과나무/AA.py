#import sys
#sys.stdin = open("input.txt","rt")

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
sum=0

for i in range(n//2):
    for j in range(n//2-i,n//2+i+1):
        sum+=arr[i][j]
    for k in range(n//2-i,n//2+i+1):
        sum+=arr[n-1-i][k]

for j in range(n):
    sum+=arr[n//2][j]

print(sum)