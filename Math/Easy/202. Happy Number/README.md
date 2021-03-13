# 202. Happy Number

## Problem Statement

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

## Main Concept

**Seen values** - The infinite loop in the algorithm can safely be terminated once we see a number again which we have seen previously.

## Challenge

Keeping track of all seen values.

## Solution Explained

We write a function to perform the operations described in the question.

Then we run the function till it either yields a 1, in which case we return true, or when we see a value we have already seen before. I have used a set to keep track of the seen values.
