#import sys

#sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
li = list(map(int,input().split()))
count=0

for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=li[j]
        if sum==m:
            count+=1
            break
        elif sum>m:
            break
    if sum<m:
        break








print(count)
