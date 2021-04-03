# 3. Longest Substring without Repeating Characters

## Problem Statement

Given a string s, find the length of the longest substring without repeating characters.

## Main Concept

**Hash Set** - A hash set is a data structure which supports O(1) look up and insert operations.

## Solution Explained

We maintain two pointers at the the start and end of our window. We traverse through the given string adding characters to our set if they are not in our set. We keep a track of the maximum size of our set. When we come across an element in our set we decrease the size of our window by one from the left and delete the left most element from our set.
