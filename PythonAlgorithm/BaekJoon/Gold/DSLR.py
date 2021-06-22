import sys
from collections import deque

sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A,B = input().split()
    q = deque([[deque([a for a in A]),['']]])
    while q:
        regi,oper = q.popleft()
        regi_R = regi.copy()
        regi_L = regi.copy()
        regi_L.rotate(-1)
        regi_R.rotate(1)
        
        if int(''.join(regi_L))%10000 == int(''.join(B))%10000:
            break
        if int(''.join(regi_R))%10000 == int(''.join(B))%10000:

