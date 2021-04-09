# 106. Construct Binary Tree from Inorder and Postorder Traversal

## Problem Statement

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

## Solution Explained

This solution is similar to [105. Construct Binary Tree from Preorder and Inorder Traversal](../105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal).

The only difference here is that while making the call for the left subtree we ignore all the elements in the right subtree in our postorder array.
