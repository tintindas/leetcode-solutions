# 111. Minimum Depth of a Binary Tree

## Problem Statement

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note**: A leaf is a node with no children.

## Solution Explained

Our base condition is to return 0 height when we try to access the subtrees of a leaf.

We recursively call for the left and right subtrees to get their height.

If both the heights of left and right subtrees are 0 we return 1.

If one of the subtrees exists and the other one does not we return the height of the subtree that exists plus one.

If both subtrees exist we return the minimum of the height of the subtrees plus one.
