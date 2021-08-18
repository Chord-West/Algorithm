import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
INF = sys.maxsize

def bellmanford(start):
    dis = [INF] * (N+1)
    dis[start] = 0
    for _ in range(N-1):
        for now,next,cost in road:
            if dis[next] > cost + dis[now]:
                dis[next] = cost+dis[now]
    for now,next,cost in road:
        if dis[next] > cost + dis[now]:
            return True
    return False

TC = int(input())
for _ in range(TC):
    N,M,W = map(int,input().split()) # N 지점의 수, M 도로의 개수, W 웜홀의 개수
    road = []
    for _ in range(M): # 도로
        s,e,t  = map(int,input().split())
        road.append((s,e,t))
        road.append((e, s, t))
    for _ in range(W): # 웜홀
        s,e,t = map(int,input().split())
        road.append((s,e,-t))
    if bellmanford(1):
        print("YES")
    else:
        print("NO")
