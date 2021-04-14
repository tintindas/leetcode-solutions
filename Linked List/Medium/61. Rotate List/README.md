# 61. Rotate List

## Problem Statement

Given the head of a linked list, rotate the list to the right by k places.

## Solution Explained

First we find the length of the linked list.

Now we take the mod of k with the length to get the real k after any number of whole rotations.

Then it is only a matter of modifying the solution of [19. Remove Nth Node From End of List](../19.%20Remove%20Nth%20Node%20From%20End%20of%20List) to rotate the list by k positions.
