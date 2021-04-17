from typing import List


class Solution:
    def twoSum(self, nums, target):
        seen = set()
        for num in nums:
            if target - num in seen:
                self.ans.add((-target, num, target - num))
            seen.add(num)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        nums.sort()

        for i in range(len(nums)):
            self.twoSum(nums[i + 1 :], -nums[i])

        return list(self.ans)