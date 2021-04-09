# 103. Binary Tree Zig Zag Level Order Traversal

## Problem Statement

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

## Challenges

Flipping the order of visiting nodes.

## Solution Explained

We solve this problem using two doubly-ended queues.

We augment a simple BFS traversal of a tree with some logic to flip the order we visit nodes in i.e. left to right or right to left.

First we initialise a queue and put the root of the tree in it.

While there are elements in the queue:

- We initialise a queue `q_next` which will hold the elements of the next level.

- `level` array keeps track of our traversal of that level. It is appended to the answer array once we have completely processed a level.

- If we are traversing from left to right we pop from the front of the queue and that becomes our node. For each node we store the left and right nodes in `q_next`.

- If traversing from right to left we pop from the end of the queue to get our node and then insert the right and left nodes, in that order, into the front of `q_next`.

- The previous two points are done in this way to always maintain a left to right order of nodes in `q_next`. This helps to traverse in both forward and reverse directions.

- Once a level has been completely processed we add the level array to our answer array and make `q_next` our main queue and reverse the direction of traversal.
