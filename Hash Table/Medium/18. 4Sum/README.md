# 4Sum

## Problem Statement

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

**Notice** that the solution set must not contain duplicate quadruplets.

## Main Concept

**kSum** - We have already done the 2Sum problem which is trivial using hash sets. In this solution we are asked to generalise this solution to kSum (or 4Sum). We do this using recursion.

## Solution Explained

We write a function 2Sum which is the same solution as in [Two Sum](../../../Array/Easy/1.%20Two%20Sum). The one modification made to the function is a check to see if there are any duplicates. Duplicates are not added into the results array.

We write a function kSum which will help us generalise the 2Sum solution for any k. The base condition for our recursive calls of this function is if `k==2` in which case we will return the `twoSum` call as is.

For `k > 2` we make recursive calls for each element of the array with `k` being decremented each time and `target = target - element`. The array passed to the call has all elements to the right of the element being processed.

The time complexity of this solution is O(N^k-1) for a given k. For 4Sum we have the time complexity O(N^3).
