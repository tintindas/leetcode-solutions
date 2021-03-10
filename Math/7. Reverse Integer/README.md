# 7. Reverse Integer | Easy | Math

## Problem Statement

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

## Main Concept

Integer overflows - If the number of bits used is fixed, the range of integers that can be represented would be fixed and can potentially overflow. That is the case for many languages such as C/C++. (Not the case for python)

## Challenges

1. Keeping reverse within bounds i.e. within [-2^31, 2^31 - 1] or return 0.
2. Keeping track of sign of the number.

## Explanation

1. Check to see if the input number is within the valid range.
2. In each loop check to see if ans is less than max_int i.e. 2^31 before doing the multiplication operation.
3. Keep track of the sign of the number in a separate variable.

## Notes

1. Easier in python as integer overflows are handled automatically in the language. Indeed the language as arbitrary precision and hence pure python does not have integer overflows at all. (However numpy and pandas do. Watch out for that)
2. Problem is trickier in C++ or Java. Solve with those languages to understand handling of integer overflows which is what this problem is meant to teach.
