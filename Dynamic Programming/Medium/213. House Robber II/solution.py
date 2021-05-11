from typing import List


class Solution:
    def helper(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        value1 = self.helper(nums[:-1])
        value2 = self.helper(nums[1:])

        return max(value1, value2)
