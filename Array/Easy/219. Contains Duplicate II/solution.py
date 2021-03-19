from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        s = set(nums[:k])

        if len(s) < k and k <= n:
            return True

        if k > n and len(s) < n:
            return True

        for i in range(k, n):
            if nums[i] in s:
                return True

            s.add(nums[i])
            s.discard(nums[i - k])

        return False
