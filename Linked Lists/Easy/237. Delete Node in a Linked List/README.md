# 237. Delete Node in a Linked List

## Problem Statement

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

## Challenges

We do not have a reference to the previous node of the given node.

## Solution Explained

We write the value of the given node with the value of the next node. Then we delete the node next to the given node.
