# 112. Path Sum

## Problem Statement

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

## Solution Explained

The first check is a guard clause to check if we have been passed the root of a tree at all or not.

Then we check to see if we are at a leaf node. If we are:

- We return true if the leaf node is the same as our target sum.
- We return false otherwise

We make recursive calls for the left and right subtrees with the value of the current node subtracted from the target sum.
