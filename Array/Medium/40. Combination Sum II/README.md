# 40. Combination Sum II

## Problem Statement

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

## Solution Explained

We have two choices for every element. We can either include it in the sum or we can exclude it.

We write a function to generate this decision tree.

Every time we exceed the target we stop searching that branch of the tree.

When we find a path that sums up to the target we add it to our answer array.
