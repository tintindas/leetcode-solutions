# 36. Valid Sudoku

## Problem Statement

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
1. Each column must contain the digits 1-9 without repetition.
1. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.1.

## Main Concept

**Sets** - We need to use many sets in this solution to keep track of the elements we have seen in each row, column and box.

## Solution Explained

This is a really simple solution.

We declare a set for each row, column and 3x3 box.

Then we traverse through the board one cell at a time. Checking to see if we have seen the current element before in its row, column or box before. If we have our Sudoku configuration is invalid. If we have not seen the element before we add it to the respective sets for its row, column, and box.
