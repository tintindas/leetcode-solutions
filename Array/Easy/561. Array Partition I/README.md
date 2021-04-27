# 561. Array Partition I

## Problem Statement

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

## Solution Explained

We sort the array and then add up alternate elements as for each pair of elements the left elements will be the minimum of the two.
