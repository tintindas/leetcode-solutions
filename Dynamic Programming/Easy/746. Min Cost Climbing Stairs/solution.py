from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        second_last = cost[0]
        last = cost[1]
        for i in range(2, len(cost)):
            c = min(last, second_last) + cost[i]
            second_last = last
            last = c

        return min(last, second_last)