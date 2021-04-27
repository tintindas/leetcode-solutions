# 228. Summary Ranges

## Problem Statement

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

- "a->b" if a != b
- "a" if a == b

## Solution Explained

We look at the previous element in our list and if it is not one less than our current element we have a range. We keep a track a start and end of each range and update the start and end variables whenever we push a range to our answer array. We update the end on every iteration.
