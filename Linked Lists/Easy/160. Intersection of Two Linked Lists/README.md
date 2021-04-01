# 160. Intersection of Two Linked Lists

## Problem Statement

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

## Solution Explained

We find the lengths of the two linked lists.

We then account for the difference in lengths of the lists by discarding `abs(lenA - lenB)` number of nodes from the longer list.

We then traverse both lists one node at a time till we find the point of intersection and return that node.

If no point of intersection is found we return `None`.
