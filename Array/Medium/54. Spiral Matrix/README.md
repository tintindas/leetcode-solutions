# 54. Spiral Matrix

## Problem Statement

Given an m x n matrix, return all elements of the matrix in spiral order.

## Solution Explained

We keep a track of the rows and columns that form the outer edge of the matrix i.e. the left, right, top and bottom.

As we print the elements we draw the boundaries inwards. When the boundaries cross we have printed all the elements.
