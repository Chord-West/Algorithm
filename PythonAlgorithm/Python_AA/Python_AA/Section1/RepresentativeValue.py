import sys

#sys.stdin=open("input.txt","rt")

n = int(input())
grade=list(map(int,input().split()))
ave=round(sum(grade)/n)
min=2147000000

for idx, x in enumerate(grade):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1

print(ave, res)