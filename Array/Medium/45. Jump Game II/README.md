# 45. Jump Game II

## Problem Statement

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

## Solution Explained

We find the left and right boundaries of the next step.

The left boundary is given by the previous step's right boundary plus 1.

The right boundary is given by the maximum reach of an element in a step, which is calculated as the index plus the element at the index.

We repeat these steps till we reach the final index of the array.
