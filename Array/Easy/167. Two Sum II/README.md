# 167. Two Sum II - Input array is sorted

## Problem Statement

Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.

## Solution Explained

The input array is sorted therefore we can solve this problem using the **two pointer** method.

Declare two pointers at index 0 and the end index of the given array.

If the sum of the numbers at index `i` and `j` is:

1. equal to `target` then we return `[i+1, j+1]`
2. greater than `target` then we decrement `j`
3. less than `target` then we increment `i`

We do this while `i` is less than `j`.
