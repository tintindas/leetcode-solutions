# 83. Remove Duplicates from Sorted List

## Problem Statement

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## Solution Explained

We declare two pointers

```
prev = head
curr = head.next
```

While `curr` and `prev` both have the same value we increment `curr`. If they have different values we point the next of `prev` to `curr` and then increment the prev pointer.

Finally, we point the next of `prev` to `None` to handle any duplication at the end of the list.

We return the `head` of the list.
