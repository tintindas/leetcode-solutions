# 34. Find First and Last Position of Element in Sorted Array

## Problem Statement

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

**Follow up**: Could you write an algorithm with O(log n) runtime complexity?

## Solution Explained

We define two functions which are modifications to binary search.

The first function returns when we find the left most occurrence of the target element. Here, we modify the binary search algorithm to stop if the target is found and the element to the left of target either does not exist or is different from the target.

We make a similar modification to the other function to find the rightmost occurrence of the target element.
