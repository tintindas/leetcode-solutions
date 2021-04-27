# 414. Third Maximum Number

## Problem Statement

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

## Solution Explained

We take the distinct numbers of the array, sort them and return the third last number.

## Notes

- Time complexity of this approach is O(nlogn)
- The heap approach is O(nlogn).
- We can solve this in O(n) too.
