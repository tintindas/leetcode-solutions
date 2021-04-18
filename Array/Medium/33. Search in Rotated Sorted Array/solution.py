from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[hi]:
                if target < nums[lo] or target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            if nums[mid] < nums[hi]:
                if target > nums[hi] or target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1
