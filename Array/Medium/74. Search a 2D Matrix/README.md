# 74. Search a 2D Matrix

## Problem Statement

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

## Solution Explained

We start at the upper right corner of the matrix.

While we are within the bounds of the matrix:

- If we find our target we return `True`.
- If the target is greater than the element at our position then it cannot be on the current row.
- If the element is smaller than the target it must be in the current row or not exist in our matrix at all as we have excluded all the previous rows from our search space.
