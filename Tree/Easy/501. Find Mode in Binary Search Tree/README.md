# 501. Find Mode in Binary Search Tree

## Problem Statement

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

## Main Concept

**Inorder Traversal of BST** - The inorder traversal of a BST is always in sorted order.

## Solution Explained

We do an inorder traversal of the BST and keep track of the count of times we have seen the same element. And a track of the maximum count we have seen.

We keep a track of the previous number we have seen and if we see the number again we add 1 to the count. If we see a different number we reset the count to zero.

When our count exceeds the maximum count we make the maximum count our current count, empty our `modes` array and push the value of our current node to the `modes` array. If count becomes the same as the maximum count we add our current node's value to our `modes` array.

After every node is processed we set `prev` to the current node's value.
