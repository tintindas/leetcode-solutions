# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Main Challenges

Getting the right subtree of each node correct.

## Solution Explained

In preorder traversal we visit the root and then the left and right subtrees.

In inorder traversal we visit the left subtree then the root and then the right subtree.

So, to find the root node we look at the preorder traversal.

Once we have found the root we look at the inorder traversal to find the elements which will be in the left subtree i.e. all the elements to the left of the root value in the inorder array and the elements which will be in the right subtree i.e. all the elements which are to the right of the value of root in the inorder array.

We make recursive calls to build the left and right subtrees.

The right subtree call is of interest because to correctly make this call we must ignore all the elements in the left subtree which are in the preorder array. This can be easily done by skipping the `pre_start` variable by the number of elements in the left subtree.
