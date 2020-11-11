import sys
sys.stdin = open("input.txt","rt")

n = int(input())
f = list(map(int,input().split()))
f.sort()

result=0
count =0

for x in f:
    count+=1
    if  count>=x:
        result+=1
        count=0

print(result)
    
