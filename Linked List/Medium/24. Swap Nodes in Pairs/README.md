# 24. Swap Nodes in Pairs

## Problem Statement

Given a linked list, swap every two adjacent nodes and return its head.

## Solution Explained

This solution some careful pointer juggling

We initialise four pointers:

```
prev = None
first = head
second = head.next
next_pair = None
```

While we have pairs to swap:

- Update the `next_pair` pointer to track the first node of the next pair.

- Update `prev.next` to point to `second` if `prev` exists. If `prev` does not exist this is the first iteration and therefore `second` will become the head of our list.

- We do a pointer rearrangement to flip the order of the pair of the nodes.

- Update prev to point to the last pointer in our flipped pair.

- Update first and second to point to the first and second nodes in the next pair.
