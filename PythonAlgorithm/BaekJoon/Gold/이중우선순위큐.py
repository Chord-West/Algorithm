import sys
import heapq
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    heap=[]
    max_heap=[]
    for _ in range(int(input())):
        oper,n = input().split()
        n = int(n)
        if oper=='I':
            heapq.heappush(heap,n)
            heapq.heappush(max_heap,(-n,n))
        else:
            if len(heap)>0:
                if n==1: #최댓값 삭제
                    max_v=heapq.heappop(max_heap)[1]
                    heap.remove(max_v)
                else: # 최솟값 삭제
                    min_v=heapq.heappop(heap)
                    max_heap.remove((-min_v,min_v))
    if heap:
        print(heapq.heappop(max_heap)[1],heapq.heappop(heap))
    else:
        print("EMPTY")
