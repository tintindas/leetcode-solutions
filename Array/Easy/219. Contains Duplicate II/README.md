# 219. Contains Duplicate II

## Problem Statement

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Main Concept

**Sliding Window** - We maintain a window with k elements and check if any element repeats within the window.

## Challenges

Dealing with edge cases where k is greater than the size of the array.

## Solution Explained

- We initialise a set with the first k elements of the input array.
- Check edge cases:
  - if the size of the set is less than k and k is less than the size of input array then a number must be duplicate in the first k elements of the input array.
  - if k is greater than the length of the array and the size of the set is less than the size of the input array then there must be a repeated element in the array.
- For elements in the array from index `k` to `n-1`, we check if the element already exists in the set. If it does we return `True`. If it does not we move the window 1 space to the right by inserting the element currently being processed and removing the leftmost element of the window, thereby maintaining the a constant size of the set i.e. `k`.
