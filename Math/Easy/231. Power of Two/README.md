# 231. Power of Two

## Problem Statement

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

## Main Concept

**Powers of Two** - Identifying powers of two is as easy as counting the number of ones in a the numbers binary representation. All powers of two only have one '1' in their binary representation.

## Challenges

None

## Solution Explained

The easiest solution to this problem is to initialise a variable, _i_ as 1 and then keep multiplying it by 2 while it is less than n and checking equality in each iteration.

## Notes

1. Another very easy solution is to convert the number into binary and then count the number of ones in the binary string.
