import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    s,e= map(int,input().split())
    max=219000
    ch = [0]*(max+1)
    dis = [0] * (max + 1)
    ch[s]=1
    dq = deque([s])
    while dq:
        x = dq.popleft()
        if x==e:
            break
        for ne in(x-1,x+1,x+5):
            if 0<ne<=max:
                if ch[ne]==0:
                    dq.append(ne)
                    ch[ne]=1
                    dis[ne]=dis[x]+1
    print(dis[e])