# 206. Reverse Linked List

## Problem Statement

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Solution Explained

We traverse the linked list from `head` flipping the pointers as we go along.

After the last iteration we have flipped all the pointers except for the last one which we flip outside the loop.

We return `curr` which at that point is the start of the reversed linked list.
