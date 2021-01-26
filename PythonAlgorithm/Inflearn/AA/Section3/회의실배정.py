#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
arr=[]
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

arr.sort(key=lambda x:x[1])
cp = arr[0][1]
sum = 1
for i in range(1,n):
    if arr[i][0]<cp:
        continue
    else:
        sum+=1
        cp=arr[i][1]

print(sum)
