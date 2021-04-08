# 543. Diameter of Binary Tree

## Problem Statement

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Solution Explained

In this solution we are just augmenting the function to calculate the height of the node with some extra functionality.

We initialise the diameter as zero. We then recursively call the `longest_path` function for each node.

For each node we calculate the longest paths in the left and right subtrees i.e. the heights. We then overwrite the `diameter` variable with the combined total of the heights of the left and right subtrees if the total is greater than the current diameter. This takes care of the case when the diameter does not pass through the root of the tree.

Finally, we return the height of the current node from within the `longest_path` function.

From the main function we return the calculated diameter of the binary tree.
