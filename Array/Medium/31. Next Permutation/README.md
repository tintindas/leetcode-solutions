# 31. Next Permutation

## Problem Statement

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

## Solution Explained

We find the first non-increasing number from the end of the array at index `idx`.

We swap this number with the number just greater than it to its right.

Then we reverse the numbers from the `idx` to the end of the array to get the next permutation of the given number.
