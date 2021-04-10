# 116. Populating Next Right Pointers in Each Node

## Problem Statement

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

## Solution Explained

A simple level order traversal of the tree.

For each level we point the next pointer to the next node in the queue. When we reach the last node in a level we point it none.

## Notes

117. Populating Next Right Pointers in Each Node II is the same question for some reason.
