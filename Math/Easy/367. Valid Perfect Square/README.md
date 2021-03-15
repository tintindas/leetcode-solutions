# 367. Valid Perfect Square

## Problem Statement

Given a positive integer num, write a function which returns True if num is a perfect square else False.

**Follow up: Do not** use any built-in library function such as sqrt.

## Main Concept

**Binary Search** - If the given number is a valid perfect square there will exist an integer in the range [1, n] which will be its sqaure root. We can search the range with binary search.

## Solution Explained

We take 1 as the lower bound and the given number as the upper bound. To perform a binary search we reduce the search space by half in every iteration.

We calculate `mid = (lo + hi)//2`

- If `mid*mid == num`, the given number is a valid perfect square.

- If `mid*mid > num`, we discard the right half of the search space.

- If `mid*mid < num` we discard the left half of the search space.

If `hi` goes below `lo` we end the search and return `False`.
