# 2. Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Solution Explained

We traverse both the linked lists to add the two numbers together.

We take one digit from `l1` while there are still digits remaining in `l1` else we take zero. We do the same with `l2`.

Once we have both the digits we add them.

We create a new node with the one's place digit of our sum. And update our carry to hold the ten's place digit.

We connect the previous node with this node.

Then we increment the pointers of `l1` and `l2` by one.

If after we have processed all the elements of both lists there remains a carry we initialise a node with the carry and then add it to the linked list.
