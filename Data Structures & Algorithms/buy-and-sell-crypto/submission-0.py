class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0.0
        minSofar = float('inf')
        for price in prices:
            minSofar = min(minSofar, price)
            profit = max(profit, price - minSofar)

        return int(profit)
        