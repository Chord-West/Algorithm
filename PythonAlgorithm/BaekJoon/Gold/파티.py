import sys
import heapq
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

N,M,X = map(int,input().split())
INF = sys.maxsize
road =[[] for _ in range(N+1)]

def dijkstra(start):
    node[start]=0
    heap=[]
    heapq.heappush(heap,(0,start))
    while heap:
        now_cost,now_node = heapq.heappop(heap)
        if node[now_node] < now_cost:
            continue
        for next_cost,next_node in road[now_node]:
            next_cost += now_cost
            if next_cost < node[next_node]:
                node[next_node] = next_cost
                heapq.heappush(heap,(next_cost,next_node))


for _ in range(M):
    a,b,cost= map(int,input().split())
    road[a].append((cost,b))
ans_node = [0]*(N+1)
for i in range(1,N+1):
    node = [INF] * (N + 1)
    dijkstra(i)
    if i==X:
        ans_node=[a+b for a,b in zip(ans_node,node)]
    else:
        ans_node[i]+=node[X]
ans_node[0]=-1
print(max(ans_node))