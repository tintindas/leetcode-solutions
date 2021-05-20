from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        d = {}
        max_length = 0
        d[0] = -1
        for idx, num in enumerate(nums):
            count = count + 1 if num == 1 else count - 1

            if count not in d:
                d[count] = idx
            else:
                l = idx - d[count]
                max_length = max(l, max_length)

        return max_length
