# 82. Remove Duplicates from Sorted List II

## Problem Statement

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

## Solution Explained

We declare a variable `pre_head` whose next pointer points to the node that will be the head of our result linked list.

Then it is a simple matter of redirecting pointers after skipping the repeating values.

We keep a track of the previous value before the sublist of repeating values and point the next pointer of this node to the node after the sublist of repeating values.
