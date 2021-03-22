from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = {}
        stack = []

        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        for num in stack:
            mapping[num] = -1

        return [mapping[n] for n in nums1]