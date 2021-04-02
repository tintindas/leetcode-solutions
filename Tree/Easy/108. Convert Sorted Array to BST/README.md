# 108. Convert Sorted Array to BST

## Problem Statement

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Solution Explained

The root of our BST will always be the middle value of our sorted array in order for the BST to be balanced.

We place the mid value of the array as the root. Then we make recursive calls for the left subtree passing in the array till mid and the right subtree passing in the array from mid+1 to end.

Our recursion ends when we pass in an empty array to our function.
