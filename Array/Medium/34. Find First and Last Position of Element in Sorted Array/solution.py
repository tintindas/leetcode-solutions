from typing import List


class Solution:
    def find_first(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                if mid > 0 and nums[mid - 1] == target:
                    hi = mid - 1
                else:
                    return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def find_last(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid + 1] == target:
                    lo = mid + 1
                else:
                    return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_first(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.find_last(nums, target)
        return [left, right]