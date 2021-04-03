# 138. Copy List with Random Pointer

## Problem Statement

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

## Challenges

The challenge with making a deep copy of a linked list or graph is that one has to maintain a mapping from the original node to the new node in order to keep the pointers pointing to the correct nodes in our copy.

## Solution Explained

We pass through the linked list once making a copy of all the nodes and mapping the original nodes to the new nodes.

On our second pass through the linked list we make our links both for the next and the random pointers. This is now a trivial task as we only have to check if our original node has a next or random pointer and then make a new link from our new node to the node pointed to by our mapping for `node.next` and `node.random`.
