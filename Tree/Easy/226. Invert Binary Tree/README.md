# 226. Invert Binary Tree

## Problem Statement

Given the root of a binary tree, invert the tree, and return its root.

## Solution Explained

We make recursive calls for the left and right subtrees.

We assign the returned calls to the opposite subtrees i.e. we assign the `invertTree` call of the right subtree to `root.left` and vice versa.
