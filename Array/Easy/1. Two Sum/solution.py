from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in s:
                return [i, s[complement]]
            s[nums[i]] = i

        return {0, 0}
