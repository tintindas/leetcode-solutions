# 39. Combination Sum

## Problem Statement

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

## Solution Explained

We decide on the path we take to get to our target.

At any moment we can make two choices either to include the element at our index or to not include it.

If we do not include the number then we move on to the index.

If we do include the number we can include it again or not include it.

We generate the decision tree of our choices by making two recursive calls, one which does not include the number at our index and another that does include the number at our index.
