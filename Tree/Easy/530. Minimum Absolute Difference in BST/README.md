# 530. Minimum Absolute Difference in BST

## Problem Statement

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

## Main Concept

**Inorder Traversal of BST** - The inorder traversal of a BST is always in sorted order.

## Solution Explained

This solution is very similar to [501. Find Mode in BST](../501.%20Find%20Mode%20in%20Binary%20Search%20Tree).

We keep a track of the previously seen number in the inorder traversal and the minimum difference seen.

We return the minimum difference once we have traversed through the whole tree.
