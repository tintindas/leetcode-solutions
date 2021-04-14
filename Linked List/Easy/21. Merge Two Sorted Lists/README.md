# 21. Merge Two Sorted Lists

## Problem Statement

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

## Main Concept

**Linked Lists** - Linked Lists are a data structure which can store related data in discontinuous memory locations. A node of a linked list stores the data as well as a reference to the next memory location in the list.

## Solution Explained

We are given two linked lists.

We initialise a pointer `head` which will point to our current position in the linked list. `start` points to the start of our list.

For the two lists we check which element is smaller and add it to our linked list by pointing the next pointer of the previous node to the lesser element of either `l1` or `l2`. Then we increment the pointer of the list whose element has been added to the linked list. Then `head` is incremented to point to our most recently processed node.

If one of our lists is entirely processed we point the next pointer of the linked list to the other list.

We return the pointer which points to starting node of our linked list.
