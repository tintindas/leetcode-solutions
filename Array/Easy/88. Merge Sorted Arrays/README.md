# 88. Merge Sorted Arrays

## Problem Statement

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

## Solution Explained

We use three pointers to approach this problem

1. `i` points to the end of `nums1`, i.e. the last number of `nums1`.
1. `j` points to the end of `nums2`.
1. `k` points to the end of `nums1`, i.e the last zero.

We place the greatest element of `nums1[i]` and `nums2[j]` at index `k` in `nums1`. Either `i` or `j` is decreased depending on which had the gretest element at the index. `k` is decreased after every iteration. When one array is completely processed we place the remaining elements of the other (if any) in order.
