# 120. Triangle

## Problem Statement

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

## Solution Explained

We traverse the triangle from bottom to top. We start at the last but one row and add the minimum of the two choices we can make from any element to the element. We do this for all the rows till the top. Our answer is the topmost element of the triangle.
