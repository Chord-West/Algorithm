#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))
res =[ 0 for _ in range(n)]
for idx,x in enumerate(num):
    count = 0
    i = 0
    while True:
        if count==x and res[i]==0:
            break
        if res[i]==0:
            count+=1
            i+=1
        else:
            i+=1

    res[i]=idx+1

for x in res:
    print(x,end=' ')

