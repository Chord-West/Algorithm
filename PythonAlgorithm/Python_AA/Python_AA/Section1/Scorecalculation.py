import sys

#sys.stdin = open("input.txt","rt")

n = int(input())
score=list(map(int,input().split()))

sum=0
count=0
for i in range(len(score)):
    if(score[i]==1):
        count+=1
    else:
        count=0
    sum= sum+count*score[i]

print(sum)
