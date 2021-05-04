# 79. Word Search

## Problem Statement

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Solution Explained

We look for the first letter of the given word and when we find it we do a dfs search from that position for the next letter and so on. If we find all the letters of the word then we return `True`.

Our `dfs` function has a guard clause that returns `False` if our search goes out of bounds of the matrix or the letter we are at is not the letter we are looking for in the word.

We make the cell we are currently at empty so that our dfs search does visit the cell it has come from.

We restore the cell when the execution returns to the calling function.
