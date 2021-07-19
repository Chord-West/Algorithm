from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # K : 경유지
        # src = 시작
        graph = defaultdict(list)

        for a, b, cost in flights:
            graph[a].append((b, cost))

        heap = [(0, src, k)]
        while heap:
            cost, now, k = heappop(heap)
            if now == dst:
                return cost
            if k >= 0:
                for next_node, next_cost in graph[now]:
                    alt = next_cost + cost
                    heappush(heap, (alt, next_node, k - 1))

        return -1

