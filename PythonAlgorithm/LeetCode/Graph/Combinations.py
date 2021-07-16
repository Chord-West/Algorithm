# Runtime 76ms

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(combinations(range(1, n + 1), k))

        return arr