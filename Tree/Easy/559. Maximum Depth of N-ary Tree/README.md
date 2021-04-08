# 559. Maximum Depth of N-ary Tree

## Problem Statement

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Solution Explained

We do simple DFS traversal of the tree returning the depth in a bottom up manner with each recursive call i.e. leaves have `depth = 1`, their parents have `depth = 2` and so on.
