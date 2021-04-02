# 100. Same Tree

## Problem Statement

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Solution Explained

To check if the two trees are the same we check that the value of the two nodes are the same and then we recursively check if the left and right subtrees of the respective nodes are also identical.

The base conditions to our recursion are that either both `p` and `q` pointers hit `None` simulataneously in which case we return `True`. One of the nodes become `None` in which case the trees are not identical.
