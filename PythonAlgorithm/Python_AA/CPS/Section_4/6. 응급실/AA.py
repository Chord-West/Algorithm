#import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

if __name__ =="__main__":
    n,m = map(int,input().split())
    p=[[int(x),0]for x in input().split()]
    dq=deque(p)
    dq[m][1]=1
    count=0
    while dq:
        for i in range(1,len(dq)):
            if dq[0][0]<dq[i][0]:
                dq.append(dq.popleft())
                break
        else:
            x=dq.popleft()
            count+=1
            if x[1]==1:
                print(count)
                break


