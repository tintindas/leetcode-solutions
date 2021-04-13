# 392. Is Subsequence

## Problem Statement

Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

## Solution Explained

We traverse through `t` and every time we see the same character as in `s` we increment `s_index`.

If `s_index` reaches the end of `s` then we return `True` else `False`.
