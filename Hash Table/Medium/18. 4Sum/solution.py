from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s = set()

        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
                s.add(nums[i])

        return res

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []

        if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
            return res

        if k == 2:
            return self.twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for _, s in enumerate(self.kSum(nums[i + 1 :], target - nums[i], k - 1)):
                    res.append([nums[i]] + s)

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        return self.kSum(nums, target, 4)
