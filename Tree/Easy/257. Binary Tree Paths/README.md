# 257. Binary Tree Paths

## Problem Statement

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

## Solution Explained

We do a simple Depth First Search to solve this problem.

We initialise a stack that keeps track of our nodes and paths.

We put the root node and an empty path into our stack.

While there are elements in our stack:

- If we reach a leaf node we append the current path to our answer array
- If there is a left subtree we put the root of the left subtree and the path uptil now into our stack. We do the same if there is a right subtree.

We return our answer array.
