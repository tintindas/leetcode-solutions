# 67. Add Binary

## Problem Statement

Given two binary strings a and b, return their sum as a binary string.

## Main Concept

**Adding digit by digit** - Adding digit by digit must be carried out from the right hand side and carry must be maintained through out the operation.

## Challenges

1. Carrying out right to left operations can be done via keeping track of a pointer for each of the input strings. The pointers point to the digits currently being processed. They are started at the right most digit.
2. Maintaining carry - In the binary number system, anything above a 1 will generate a carry.
3. Maintaining answer in order. I have used a deque in this solution due to its ability to have insertions from both ends.

## Solution Explained

Maintain two pointers which denote the digits being processed of the two given strings. Initialise carry as zero and an empty deque.

Process element by element while there are still elements left in either string or there is still a carry.

Return contents of deque as a string.

## Notes

1. Could be done solved using an array too.
