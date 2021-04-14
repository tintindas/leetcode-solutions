# 404. Sum of Left Leaves

## Problem Statement

Find the sum of all left leaves in a given binary tree.

Example:

```
    3
   / \
  9  20
    /  \
   15   7
```

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

## Solution Explained

We initialise a stack to keep a track of the nodes we have to visit.

We keep going to the left subtree. When we reach a leaf we add the value of the leaf to the answer.

If the node is not a left leaf then we add it to the stack to visit later.
