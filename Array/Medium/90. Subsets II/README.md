# 90. Subsets II

## Problem Statement

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Solution Explained

Similar to [78. Subsets](../78.%20Subsets).

The only modifications we make is that the path is a tuple instead of a list as lists are mutable and tuples are not. This is done as our answer is stored in a set which requires its elements to be hashable. A set is used so that we do not have any duplicates.
