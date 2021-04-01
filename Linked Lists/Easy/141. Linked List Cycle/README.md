# 141. Linked List Cycle

## Problem Statement

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## Solution Explained

We initialise a `slow` and a `fast` pointer.

The slow pointer moves one node at a time and the fast pointer moves two nodes at a time. If there is a cycle the slow and fast pointers will eventually point to the same node.
