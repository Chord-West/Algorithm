import sys
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = deque()
        INF = -sys.maxsize
        current_max = INF
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if current_max == INF:
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = INF
        return results