# 78. Subsets

## Problem Statement

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Solution Explained

We have two choices for each element we can either include it in our current set or not include it in our current set.

We recursively build a decision tree for each index i.e. we make two calls for every index, one including the element and the other excluding it.

When we have considered all elements of our array we are at the leaf of our tree. We go no further and append the current subset to our answer list.
