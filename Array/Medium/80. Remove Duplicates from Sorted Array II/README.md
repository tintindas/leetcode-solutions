# 80. Remove Duplicates from Sorted Array II

## Problem Statement

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

## Solution Explained

Similar to [26. Remove Duplicates from Sorted Array](../../Easy/26.%20Remove%20Duplicates%20from%20Sorted%20Array).

All we modify is checking the element two elements to the left of the end of our current array instead of the element just to the left.
