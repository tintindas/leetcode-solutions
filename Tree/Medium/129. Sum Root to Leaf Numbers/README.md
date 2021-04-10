# 129. Sum Root to Leaf Numbers

## Problem Statement

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.

## Solution Explained

A simple DFS traversal while keeping a track of the elements in our DFS traversal stack.

When we get to a leaf node we convert the digits in our stack to a number and add it to our answer.
