# 63. Unique Paths II

## Problem Statement

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

## Solution Explained

Solution is very similar to [62. Unique Paths](../62.%20Unique%20Paths) and uses the same recursive formula.

We modify the base cases that is the first row and column cases. If we encounter an obstacle in the first row or column we can't reach anything further therefore everything to the right in case of the first row and below in case of the first column of the obstacle would be unreachable and therefore we can consider those cells to be obstacles too.

Then it is a simple matter of calculating the number of ways to get to every cell which is not an obstacle.
