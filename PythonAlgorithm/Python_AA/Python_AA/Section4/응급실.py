import sys
from collections import deque
sys.stdin = open("input.txt","rt")

if __name__ =="__main__":
    n,m = map(int,input().split())
    p=[ (pos,val) for pos,val in enumerate(list(map(int,input().split())))]
    dq=deque(p)
    count=0
    while True:
        cur=dq.popleft()
        if any(cur[1]<x[1] for x in dq):
            dq.append(cur)
        else:
            count+=1
            if cur[0]==m:
                print(count)
                break


