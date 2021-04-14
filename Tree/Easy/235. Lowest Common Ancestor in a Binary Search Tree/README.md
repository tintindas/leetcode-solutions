# 235. Lowest Common Ancestor in a Binary Search Tree

## Problem Statement

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Main Concept

**BST** - A BST is structured in such a way that all elements to the left of a node have smaller values than the node itself and all elements to the right of the node have values larger than the value of the node.

## Solution Explained

We check if both p and q are present in the same subtree i.e. they are either both in the left subtree or right subtree and then make a recursive call for that subtree.

If however both nodes are in different subtrees then we have found their lowest common ancestor which is the node we are at at the moment. Therefore, we return the node as our answer.
