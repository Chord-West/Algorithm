import sys
from collections import deque
sys.stdin = open("input.txt","rt")

q=deque()
for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().split()
    if x[0]=='push_front':
        q.appendleft(int(x[1]))
    if x[0] == 'push_back':
        q.append(int(x[1]))
    elif x[0]=='back':
        if len(q)>0:
            print(q[-1])
        else:
            print(-1)
    elif x[0]=='front':
        if len(q)>0:
            print(q[0])
        else:
            print(-1)
    elif x[0]=='size':
        print(len(q))
    elif x[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif x[0]=='pop_front':
        if len(q)>0:
            print(q.popleft())
        else:
            print(-1)
    elif x[0]=='pop_back':
        if len(q)>0:
            print(q.pop())
        else:
            print(-1)