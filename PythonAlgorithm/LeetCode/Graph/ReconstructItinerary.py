from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(now):
            while p[now]:
                dfs(p[now].pop(0))
            ans.append(now)

        p = defaultdict(list)
        for fr, to in sorted(tickets):
            p[fr].append(to)

        ans = []
        dfs("JFK")
        return ans[::-1]
