# 98. Validate Binary Search Tree

## Problem Statement

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

## Main Concept

**Bounding Values** - In a BST when going to the left values of the subtree are upper bounded by the value of the node where the subtree is rooted. Likewise, when going to the right the values in the subtree are lower bounded by value of the root.

## Solution Explained

We check the entire tree by making recursive calls for the left and right subtrees of each node.

If we reach a `None` value we return `True` as a non-existent subtree is by definition a BST. (as is a single node)

When going to the left we are upper bounded by `root.val`.

When going to the right we are lower bounded by `root.val`.

For every node we check if the value of the node is within `(lo, hi)`.
