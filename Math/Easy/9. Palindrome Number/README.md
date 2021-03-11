# 9. Palindrome Number

## Problem Statement

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

## Main Concept

**Handling palindromes** - The first thing to think when a palindrome question shows up is that only half of the string/number has to be processed. Processing the entire number will most likely fail a few time constrained test cases.

## Challenges

1. Handling trailing zeroes - Numbers with trailing zeroes are not generally considered palindromes.
2. Processing only half of the number.

## Solution Explained

A number cannot be a palindrome if it is negative or has trailing zeroes. I handled this with a simple guard clause.

Then keep taking the last digit from the original number and construct the reverse. Keep doing this till the original number becomes smaller than reverse.

For an even number of digits the reverse number constructed will be equal to the value left with the original number. For an odd number of digits we can ignore the last digit of the reverse number while checking equality.
