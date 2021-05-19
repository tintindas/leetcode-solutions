# 438. Find All Anagrams in a String

## Problem Statement

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

## Solution Explained

We keep a counter for the characters of the given pattern and one for the window which we are looking at.

Then we use the sliding window technique to check each window of the length of the pattern and if the counter for the window is equal to the counter for the pattern we add the starting index to our result array.

**Time Complexity**: O(length(string)\*length(pattern))
**Space Complexity**: O(length(pattern))
