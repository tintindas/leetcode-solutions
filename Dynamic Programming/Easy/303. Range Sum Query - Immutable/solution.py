from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sum = [0] * (n + 1)

        for i in range(n):
            self.sum[i + 1] = self.sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)