from typing import List


class Solution:
    def helper(self, nums, path, idx):
        if idx == len(nums):
            self.res.add(path)
            return

        self.helper(nums, path + (nums[idx],), idx + 1)
        self.helper(nums, path, idx + 1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = set()
        self.helper(nums, (), 0)
        return self.res