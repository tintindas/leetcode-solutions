# 509. Fibonacci Number

## Problem Statement

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

Given n, calculate F(n).

## Solution Explained

To calculate the nth term we only need the n-1 and n-2th terms. We keep a track of these of terms and calculate our way up from k = 2 to k = n.
