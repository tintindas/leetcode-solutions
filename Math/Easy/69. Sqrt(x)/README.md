# 69. Sqrt(x)

## Problem Statement

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

## Main Concept

**Binary Search** - The square root of a number must exist in between 1 and the number itself. Binary search can be used to find the square root.

## Challenges

The main challenge with any binary search operation is to write the correct exit clause.

## Solution Explained

The left boundary is taken as 1 and the right most boundary is taken as half of the given number. (The square root is always lesser than or equal to half of the number).

The middle of the interval is calculated. If the square of the middle element is larger than in given number then the right boundary is brought inwards. Otherwise the left boundary is brought inwards. This is repeated till the boundaries cross each other. The answer is the element pointed to by the right boundary pointer.
