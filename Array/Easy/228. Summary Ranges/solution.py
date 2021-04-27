from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = end = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - 1 == end:
                end = nums[i]
            else:
                if start == end:
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{end}")
                start = end = nums[i]

        if start == end:
            res.append(f"{start}")
        else:
            res.append(f"{start}->{end}")
        return res