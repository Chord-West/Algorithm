#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))
lt = 0
rt = n-1
x=0
str=""
tmp=[]
while lt<=rt:
    if num[lt]>x:
        tmp.append((num[lt],"L"))
    if num[rt]>x:
        tmp.append((num[rt],"R"))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        str+=tmp[0][1]
        x=tmp[0][0]
        if tmp[0][1]=="L":
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(str))
print(str)