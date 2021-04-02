# 104. Maximum Depth of a Binary Tree

## Problem Statement

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Solution Explained

The depth of any node in a given binary tree is the maximum of the heights of the left and right subtrees plus 1. We therefore calculate the height of the tree by making recursive calls for the heights of the left and right subtrees.

The base condition for our recursive calls is when we do not have a node. In which case we return `0`.
