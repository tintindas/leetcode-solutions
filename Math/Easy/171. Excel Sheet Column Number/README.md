# 171. Excel Sheet Column Number

## Problem Statement

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
```

## Main Concept

**Converting bases** - The problem asks us to convert a base 26 representation number into a base 10 number.

## Challenges

1. Keeping track of place value

## Solution Explained

We start from the right most letter in the string. Multiplying the corresponding value of the letter i.e. B = 2, A = 1 etc. with the place value gives us the contribution of the letter to the total value. We do this for every letter in the string.

In a base 10 system we get `312 = 3*10*10 + 1*10 + 2*1.`

Similarly, in a base 26 system, `ABC = 1*26*26 + 2*26 + 3*1`
