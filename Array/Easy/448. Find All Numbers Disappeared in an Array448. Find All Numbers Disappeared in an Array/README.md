# 448. Find All Numbers Disappeared in an Array

## Problem Statement

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

## Solution Explained

We take the elements from the array go to the index pointed to by that element and mark it negative indicating that `index + 1` is an element present in the array.

We make another pass through the array to find the positive elements. The `index + 1` of these elements are our missing numbers.
