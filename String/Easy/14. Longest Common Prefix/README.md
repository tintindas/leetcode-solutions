# 14. Longest Common Prefix

## Problem Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Solution Explained

We scan column wise till we find a mismatch and then return the common prefix till the index of the mismatch.
