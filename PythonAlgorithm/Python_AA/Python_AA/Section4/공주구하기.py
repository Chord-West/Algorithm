import sys
from collections import deque
sys.stdin = open("input.txt","r")

if __name__ == "__main__":
    n,k = map(int,input().split())
    dq=list(range(1,n+1))
    dq=deque(dq)
    print(dq)
    while dq:
        for _ in range(k-1):
            cur=dq.popleft()
            dq.append(cur)
        dq.popleft()
        if len(dq)==1:
            print(dq[0])
            dq.popleft()