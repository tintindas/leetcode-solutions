# 114. Flatten Binary Tree to Linked List

## Problem Statement

Given the root of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

## Solution Explained

We return if there is no node or we reach a leaf.

For non-leaf nodes we store the right subtree in a `temp` variable.

We set the left pointer to `None` and then set the right pointer to the root of the flattened left subtree (we generate this by a recursive call).

Then we traverse to the last node in the flattened subtree and attach the flattened right subtree (which we had stored in `temp`) to the the last node.
