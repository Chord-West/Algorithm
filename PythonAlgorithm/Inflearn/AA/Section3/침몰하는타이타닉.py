#import sys
#sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
w = list(map(int,input().split()))
w.sort()
sum=0
while w:
    a=w.pop()
    for idx,x in enumerate(w):
        if x+a<=m:  # 제일 큰 몸무게를 더했을 때 m보다 작으면
            a+=x
            w.pop(idx)
    sum+=1


print(sum)