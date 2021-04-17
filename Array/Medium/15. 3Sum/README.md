# 15. 3Sum

## Problem Statement

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Solution Explained

Sort the array and then run [Two Sum](../../Easy/1.%20Two%20Sum) in a loop for every element in the array.
