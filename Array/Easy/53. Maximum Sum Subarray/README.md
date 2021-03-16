# 53. Maximum Sum Subarray

## Problem Statement

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Main Concept

**Kadane's Algorithm** - If we know the max sum ending with each index of the array we can return the global maximum sum which will be the maximum sum of the contiguous array.

## Solution Explained

We initialise two variables

- `current_sum = 0`
- `max_sum = float('inf')`, this takes care of all negative arrays.

Now we process each element of the array.

For every position we calculate the maximum sum ending with that position. This is either the number at the position added to the `current_sum` or the number itself if the number is greater than `current_sum + num`. The second case will occur when `current_sum` turns negative.

We keep a track of the global maximum with the `max_sum` variable.
