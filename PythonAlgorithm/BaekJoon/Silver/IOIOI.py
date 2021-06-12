import sys
from collections import deque
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
n = int(input().rstrip('\n'))
m = int(input().rstrip('\n'))
S = input().rstrip('\n')
cnt=0
ans=0
#OOIOIOIOIIOII
for i in range(1,m-1):
    if S[i-1]=='I' and S[i]=='O' and S[i+1]=='I':
        cnt+=1
        i+=1
    else:
        cnt=0
    if cnt==n:
        ans+=1
        cnt=0


print(ans)