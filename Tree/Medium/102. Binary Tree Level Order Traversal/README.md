# 102. Binary Tree Level Order Traversal

## Problem Statement

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Main Concept

**BFS** - The solution is asking for a breadth first traversal of the tree.

## Solution Explained

We initialise a queue to keep track of the order in which we have to visit the nodes of the trees.

One of the properties of this implementation is that when we have completed traversing one level of the tree the entire next level of the tree is in our queue. This helps us determine how many nodes are in each level.

We put the root of our tree in our queue.

Then while there are elements in the queue we keep putting the children of the nodes into the queue.
