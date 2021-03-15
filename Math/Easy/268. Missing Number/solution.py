from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        array_sum = sum(nums)
        n_sum = n * (n + 1) / 2

        return int(n_sum - array_sum)