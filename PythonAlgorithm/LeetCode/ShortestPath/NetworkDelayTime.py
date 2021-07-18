from heapq import heappush, heappop
from collections import defaultdict


def networkDelayTime(times, n, k):
        network = defaultdict(list)
        dist = defaultdict(int)
        for u, v, w in times:
            network[u].append((v, w))
        heap = [(0, k)]
        while heap:
            cost, now = heappop(heap)
            if now not in dist:
                dist[now] = cost
                for v, w in network[now]:
                    next_cost = cost + w
                    heappush(heap, (next_cost, v))
        if len(dist) == n:
            return max(dist.values())
        return -1

networkDelayTime( [[2,1,1],[2,3,1],[3,4,1]], 4, 2)