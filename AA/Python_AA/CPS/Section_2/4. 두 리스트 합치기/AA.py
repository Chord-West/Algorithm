import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
a1=list(map(int,input().split()))
m = int(input())
a2=list(map(int,input().split()))

ans = a1+a2
ans.sort()
for i in range(len(ans)):
    print(ans[i],end=" ")