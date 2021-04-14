# 203. Remove Linked List Elements

## Problem Statement

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

## Challenges

1. What to do if the first elements have to be removed.

## Solution Explained

We initialise

```
prev = None
curr = head
```

Then for each element in the list we check if the value of the node matches the given value and if it does we point the next of `prev` to the the next of `curr` thereby bypassing the current node.

To deal with the issue of removing the first elements we point `head` to the next of `curr` if `prev` is `None` thereby bypassing the first node if required.
