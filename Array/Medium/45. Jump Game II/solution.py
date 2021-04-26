from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums[0] == 0 or len(nums) == 1:
            return 0

        l = r = 0
        steps = 0
        while r < len(nums) - 1:
            max_reach = r + 1
            for i in range(l, r + 1):
                max_reach = max(max_reach, i + nums[i])
            l = r + 1
            r = max_reach
            steps += 1

        return steps
