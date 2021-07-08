import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_stock=sys.maxsize
        for price in prices:
            min_stock = min(price,min_stock)
            profit = max(price-min_stock,profit)
        return profit