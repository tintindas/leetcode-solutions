from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0

        for num in nums:
            if num == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0

        return ans