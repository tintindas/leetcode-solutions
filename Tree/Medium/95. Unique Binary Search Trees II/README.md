# 95. Unique Binary Search Trees II

## Problem Statement

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

## Main Concept

**BST Property** - While generating BSTs we must keep in mind the BST property where everything in the left subtree of a node is smaller than the node and everything in the right subtree is greater than the node.

## Challenges

1. The recursive solution while intuitive is quite slow. We will speed it up using dynamic programming we will only generate a subtrees with a unique (start, end) pair once and then cache them. The next time we make this call instead of generating the all the subtrees again we can return the nodes at which the subtrees are rooted from our cache.

## Solution Explained

We declare a cache to memoize our subtrees.

The helper function works by recursively calling for the left subtrees that can be generated for a node and all the right subtrees that can be generated for a node.

We do this for every node in the range (start, end) inclusive. This way we get all the subtrees rooted at each node value from (start, end) inclusive.

Left subtree calls are made for all the values lower than the current node value and right subtree calls are made for all the values greater than current node value.

Then we generate all the trees rooted at a node by, one by one making the trees with current value as root node and going through every pair of left and right subtrees.

Everytime we generate a tree i.e. solve a subproblem we memoize it in our cache thereby speeding up our algorithm.

We return the list of all subtrees generated from our helper function.

Our helper function only runs when start is not greater than end as this condition will violate our BST property.
