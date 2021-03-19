from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        valley = prices[0]
        peak = prices[0]
        n = len(prices)
        i = 0
        while i < n - 1:

            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            max_profit += peak - valley

        return max_profit
