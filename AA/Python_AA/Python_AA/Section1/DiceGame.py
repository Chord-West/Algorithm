import sys
#sys.stdin = open("input.txt","rt")


n = int(input())
max,sum=0,0
for i in range(n):
    k = list(map(int,input().split()))
    k.sort()
    num,sn=0,0
    for j in range(len(k)-1):
        if k[j]==k[j+1]:
            num+=1
            sn=k[j]
            
    if num==0:
         sum=k[2]*100
    elif num==1:
        sum=1000+sn*100
    else:
        sum=10000+sn*1000

    if max<sum:
        max=sum

print(max)


