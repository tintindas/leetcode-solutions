# 268. Missing Number

## Problem Statement

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

**Follow up**: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

## Main Concept

**Sum of first n integers** - The sum of first n integers is given by `sum = n*(n+1)/2`

## Challenges

Using O(1) space - A trivial solution is to declare an array and marke the presence of numbers in the `nums` array in this array. However, this uses O(n) space.

## Solution Explained

We know that the sum of the first _n_ integers is given by `n*(n+1)/2`. We calculate this value.

Then we sum up the numbers in the `nums` array.

We subtract the sum of the array from the sum of the first _n_ integers. This gives us the missing number.
