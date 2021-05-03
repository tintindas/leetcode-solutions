# 75. Sort Colors

## Problem Statement

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

## Solution Explained

To sort the integers we initialise two pointers at the start and end of the array, `i` and `j` respectively.

We traverse through the array.

- When we see a 0 we swap it with the element at index `i` and then increment `i` and `k`.
- When see a 1 we do nothing and continue with our traversal.
- When we see a 2 we swap it with the element at index `j` and then decrement `j`. However, we do not move forward in our traversal of the array. This is done so that if the swap replaces our two with a 0 we can process it and send it to the front of our array.
