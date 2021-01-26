#import sys
#sys.stdin = open("input.txt","rt")
from collections import deque

if __name__ == "__main__":
    s = [x for x in input()]
    n = int(input())
    ans=[]
    dq=deque(s)
    for i in range(n):
        for x in input():
            if any( x==s for s in dq):
                ans.append(x)
        if ans==s:
            print("#{} YES".format(i+1))
        else:
            print("#{} NO".format(i + 1))
        ans.clear()
