import sys
from heapq import heappush,heappop
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline


def dijkstra(start):
    visited[start] = 0
    heap=[]
    heappush(heap,(0,start))
    while heap:
        cost, now = heappop(heap)
        if visited[now] > cost:
            continue
        for next_cost, next_node in bus[now]:
            next_cost+=cost
            if visited[next_node] > next_cost:
                visited[next_node] = next_cost
                heappush(heap,(next_cost,next_node))


INF = sys.maxsize
N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

bus = [[] for _ in range(N+1)]
visited = [INF]*(N+1)
for _ in range(M):
    a,b,cost = map(int,input().split())
    bus[a].append((cost,b))

start, end = map(int,input().split())
dijkstra(start)
print(visited[end])