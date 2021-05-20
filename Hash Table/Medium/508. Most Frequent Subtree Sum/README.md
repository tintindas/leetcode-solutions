# 508. Most Frequent Subtree Sum

## Problem Statement

Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

## Solution Explained

We propagate the sum of each subtree up the tree. For every sum we keep a count of how many times it has been seen.

We find the most common element's frequency. Then we iterate through the counter and add elements to output array when their counts match the most common elements frequency.
