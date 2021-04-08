# 563. Binary Tree Tilt

## Problem Statement

Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

## Solution Explained

We create a helper function that returns the sum of a subtree.

For every node we calculate its tilt within the helper function by making recursive calls for the sum of the left and right subtrees and then taking the absolute difference of the sums. We add the tilt to our answer variable.

Finally we return the sum of the subtree rooted at our current node from within the helper function.

Our main function returns our answer variable.
