# 139. Word Break

## Problem Statement

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Solution Explained

The problem is asking us if we can make the given word from the given dictionary with repetition allowed.

We solve the question recursively by checking if we can form some prefix of the given string with the words from the dictionary. And then calling our recursive function on the remaining string.

We memoize our recursion calls to optimise the solution.
