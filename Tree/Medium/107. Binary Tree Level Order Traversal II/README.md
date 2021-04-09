# 107. Binary Tree Level Order Traversal II

## Problem Statement

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

## Challenges

The way to avoid a O(n) reverse operation on our answer array is to initialise our answer object as a doubly-ended queue which supports O(1) append at front of the queue.

## Solution Explained

We do a simple BFS traversal of the tree and use our deque to add each level to the front of the queue thereby maintaining the required order of the question.

We convert the queue to a list before returning it as the answer.
