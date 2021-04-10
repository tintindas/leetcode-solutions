# 113. Path Sum II

## Problem Statement

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

## Solution Explained

This is a DFS problem.

We declare a stack to keep track of the elements currently in our DFS traversal.

In the helper function:

- We return if there is no node.

- When visiting a leaf node we add the stack after appending the leaf to the stack if the target sum is equal to the value of the node.

- For non-leaf nodes we add the value of the node to the stack and then make recursive calls for the left and right subtrees.

- After our recursive calls return we pop the current node from the stack and end processing that node.
