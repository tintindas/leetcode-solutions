# 110. Balanced Binary Tree

## Problem Statement

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

## Solution Explained

We define a helper function to calculate the heights of nodes.

We check if the heights of the left and right subtrees differ at most by one for the root node and also check recursively if the left and right subtrees follow the balanced property too.
