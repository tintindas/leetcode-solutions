# 1290. Convert a Binary Number in a Linked List to Integer

## Problem Statement

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

## Solution Explained

We initialise the answer as 0.

We traverse the linked list from start to end and use the formula:

```
ans = ans*base + val
```

Here our base is 2 for binary numbers.
