# 33. Search in Rotated Sorted Array

## Problem Statement

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

## Solution Explained

We can solve this by modifying a simple binary search.

- If the element at mid index is higher than the rightmost element then the target is to the right of mid if the target is less than the leftmost element or the target is greater than the mid element, else it is to the left of mid.

- If the element at mid index is lower than the highest element then the target is to the left of mid if target is higher than rightmost element or the target is lower than the mid element.
