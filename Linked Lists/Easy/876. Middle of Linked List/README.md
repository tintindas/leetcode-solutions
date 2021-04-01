# 876. Middle of Linked List

## Problem Statement

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

## Solution Explained

We use the slow and fast pointer method to solve this problem. The fast pointer moves twice as fast as the slow pointer and thus it reaches the end of the list when the slow pointer is at the middle.

We do a check before returning to determine whether the list has odd or even number of elements which determines if we return `slow` or `slow.next`.
