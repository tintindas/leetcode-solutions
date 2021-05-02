class Solution:
    def helper(self, index, path, nums):
        if index > len(nums):
            return

        if index == len(nums):
            self.res.append(path)
            return

        self.helper(index + 1, path, nums)
        self.helper(index + 1, path + [nums[index]], nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        self.res = []
        self.helper(0, [], nums)
        return self.res