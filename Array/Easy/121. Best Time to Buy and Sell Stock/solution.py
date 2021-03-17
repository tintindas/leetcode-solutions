from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, prices[i])

        return max_profit