
import sys
import heapq
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline
arr=[]

for _ in range(int(r())):
    x = int(r())
    if x == 0:
        if len(arr)>0:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr,(-x,x))
