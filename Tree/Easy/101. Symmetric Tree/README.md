# 101. Symmetric Tree

## Problem Statement

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Solution Explained

We check for symmetricity beginning with `root.left` and `root.right` subtrees.

To check for symmetricity we check if the two nodes being evaluated are equal and if the left subtree of the left node is equal to the right subtree of the right node and the right subtree of the left node is equal to the left subtree of the right node recursively.

The base conditions for our recursive calls are:

- both left and right hit `None` at the same time in which case we return `True`.
- one of left and right hits `None` in which case our tree is not symmetric and we return `False`
