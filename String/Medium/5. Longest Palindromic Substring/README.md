# 5. Longest Palindromic Substring

## Problem Statement

Given a string s, return the longest palindromic substring in s.

## Solution Explained

Our helper function gives us the longest palindromic substring with the character at the ith index as the middle.

In the main function we iterate of over the string and call the helper function for every index as the middle and also the for the space between every index as the middle.

This is done because a palindrome could have odd number of characters such as `bab` or even number of characters such as `abba`.
