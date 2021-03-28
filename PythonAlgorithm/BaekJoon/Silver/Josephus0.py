import sys
from collections import deque

sys.stdin = open("input.txt","rt")

n,k=sys.stdin.readline().split()

q = deque(x for x in range(1,int(n)+1))
ans=[]
while q:
    q.rotate(-(int(k) - 1))
    ans.append(q.popleft())
print('<',end='')
for a in ans[:-1]:
    print('%d, ' %a,end='')
print('%d>' %ans[-1],end='')