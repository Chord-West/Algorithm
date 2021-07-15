from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        p = defaultdict(int)
        for num in nums:
            p[num] += 1
        arr = sorted(p.keys(), key=lambda x: p[x], reverse=True)
        ans = arr[:k]
        return ans

