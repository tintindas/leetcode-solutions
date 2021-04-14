# 86. Partition List

## Problem Statement

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

## Solution Explained

We initialise two pointers `pre_head` and `post_head`. We will use these pointers to make two linked list one of all nodes with values less than `x` and another that has all the other nodes.

We traverse the linked list and append the nodes of the list to either the list headed by `pre_head` or `post_head` depending on their values.

After we have processed all the nodes in the list we connect the end of the list with nodes with value less than `x` to the head of the list with nodes having values greater than or equal to `x`. Then we point the end of this list to `None`.

We return `pre_head.next` which is the starting node of our answer list.
