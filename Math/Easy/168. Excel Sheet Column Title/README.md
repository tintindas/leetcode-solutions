# 168. Excel Sheet Column Title

## Problem Statement

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

**Converting bases** - The question is asking us to convert a base 10 number to a base 26 representation.

## Challenges

1. Offset - The base 26 representation begins at A -> 1 (instead of starting at 0) which introduces an offset in our counting which must be accounted for.

## Solution Explained

First, initialise a data structure that maps 1-26 to A-Z. Here we use the ascii_uppercase string from the string.py library.

We find the right most letter by getting the remainder from the number when it is divided by 26. We subtract the offset i.e. 1 from the number before division.

The number is divided by 26. Offset subtraction is done here too. This process is repeated while the number is greater than zero.

## Video Explanation

A thorough explanation is detailed in this [video](https://www.youtube.com/watch?v=UcTKk2y_3s4).
