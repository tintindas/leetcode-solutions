# 64. Minimum Path Sum

## Problem Statement

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note**: You can only move either down or right at any point in time.

## Solution Explained

The logic of this solution is very similar to [62. Unique Paths](../62.%20Unique%20Paths).

The top row and leftmost column can only be reached from the left and above respectively.

Therefore the cost to reach elements in these paths will just be a simple presum array.

Then we just calculate the cost to reach a cell by taking the minimum of coming from either the top or left and adding it to the value of the cell itself.
