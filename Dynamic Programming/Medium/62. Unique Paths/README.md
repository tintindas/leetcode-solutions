# 62. Unique Paths

## Problem Statement

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

## Solution Explained

Our robot can only move down and right so to reach any cell we can only come from the cell above it or the cell to the left of it.

So, the formula for number of ways to get to a cell (i, j) is:

```
f(i, j) = f(i-1, j) + f(i, j-1)
```

The topmost and left most rows have only one way to get to its cells i.e. either from the left or from above respectively.
