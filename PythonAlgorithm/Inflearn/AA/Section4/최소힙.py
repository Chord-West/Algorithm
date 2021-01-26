import sys
import heapq as hq
sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    tree=[]
    n=0
    while n!=-1:
        n=int(input())
        if n==0:
            if len(tree)==0:
                print(-1)
            else:
                print(hq.heappop(tree))
        else:
            hq.heappush(tree,n)