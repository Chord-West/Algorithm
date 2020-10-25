import sys
#sys.stdin=open("input.txt","rt")

T=int(input())
cnt=0
for i in range(T):
    n ,s,e,k=map(int,input().split())
    num=list(map(int,input().split()))
    ans=num[s-1:e]
    ans.sort()
    print("#%d %d"%(i+1,ans[k-1]))