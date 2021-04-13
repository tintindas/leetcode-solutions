# 303. Range Sum Query - Immutable

## Problem Statement

Given an integer array nums, find the sum of the elements between indices left and right inclusive, where (left <= right).

Implement the NumArray class:

- NumArray(int[] nums) initializes the object with the integer array nums.
- int sumRange(int left, int right) returns the sum of the elements of the nums array in the range [left, right] inclusive (i.e., sum(nums[left], nums[left + 1], ... , nums[right])).

## Solution Explained

We initialise a sum array which stores the sum till that index in at every index.

From the query function then we can just return the `sum[right+1] - sum [left]` to get the sum of range [left, right].
