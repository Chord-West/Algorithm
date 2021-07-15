from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        p = defaultdict(int)
        ans = 0
        for jewel in jewels:
            p[jewel] = 1

        for stone in stones:
            ans += p[stone]
        return ans