# 118. Pascal's Triangle

## Problem Statement

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![Pascal's Triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

## Main Concept

**Multidimensional arrays** - This problem tests our understanding of accessing data within multidimensional arrays of different sizes.

## Solution Explained

1. Declare an array `ans`.
1. Push `first_row = [1]` to `ans`.
1. For each row of the triangle:
   1. Push `1` as the first element of the row.
   1. Run a loop for `i-2` times adding up the `j-1` and `j`th elements of the previous row to get the `j`th element of the current row.
   1. Push `1` as the last element of the row.
   1. Push the row to `ans`.
