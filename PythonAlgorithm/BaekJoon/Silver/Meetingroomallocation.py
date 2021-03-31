import sys
from collections import deque
sys.stdin = open("input.txt","rt")

n = int(sys.stdin.readline())
arr=[]

for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    arr.append([s,e])
arr=sorted(arr,key=lambda x:(x[1],x[0]))
q= deque(arr)
print(q)
ch = q.popleft()[1]
cnt=1
while q:
    s,e=q.popleft()
    if ch<=s:
        cnt+=1
        ch=e
print(cnt)