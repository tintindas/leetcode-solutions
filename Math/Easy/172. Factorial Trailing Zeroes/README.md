# 172. Factorial Trailing Zeroes

## Problem Statement

Given an integer n, return the number of trailing zeroes in n!.

**Expected time complexity** - O(n)

## Main Concept

The number fives that occur in a factorial determine the trailing zeroes of the factorial.

## Challenges

Accounting for the extra fives in multiples of five such 25, 100, 125 which yield more than one 5 as a factor when factorising.

## Solution Explained

We keep dividing the given number by 5 and adding the quotient to the count of zeroes while the number is greater than zero. The repeated division of the number by 5 is to account for the numbers in the factorial which may yield more than one 5 as factors.

## Video Explanation

[Youtube Link](https://www.youtube.com/watch?v=3Hdmv_Ym8PI)
