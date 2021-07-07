import sys
from heapq import heappop, heappush
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
INF=sys.maxsize
def dijkstra(start,end):
    visited = [INF] * (N + 1)
    visited[start]=0
    heap=[]
    heappush(heap,(0,start))
    while heap:
        cost,now = heappop(heap)
        if visited[now]<cost:
            continue
        for next_cost,next in road[now]:
            next_cost+=cost
            if visited[next]>next_cost:
                visited[next]=next_cost
                heappush(heap,(next_cost,next))
    return visited[end]

N,E = map(int,input().split())
road = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,cost = map(int,input().split())
    road[a].append((cost,b))
    road[b].append((cost, a))

v1,v2 = map(int,input().split())
path1 = dijkstra(1,v1)+ dijkstra(v1,v2) + dijkstra(v2,N)
path2 = dijkstra(1,v2)+ dijkstra(v2,v1) + dijkstra(v1,N)
if path1==INF and path2 ==INF:
    print(-1)
else:
    print(min(path1,path2))
