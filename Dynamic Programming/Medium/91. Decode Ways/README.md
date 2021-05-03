# 91. Decode Ways

## Problem Statement

A message containing letters from A-Z can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

- "AAJF" with the grouping (1 1 10 6)
- "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

## Solution Explained

Every element can be considered alone or with the element next to it as there are only 26 encodings.

We initialise a `dp` array.

The first element can only be considered alone so dp[0] = 1.

The second element can be considered alone if it lies within [1, 9] and considered with the first element if the number they form lies within [10, 26].

We then run a loop from index 2 to the end index.

An element can be considered alone if it is a non-zero digit. And it can be considered with the element to its left if the number they form lies within [10, 26].

We return the last element of our `dp` array which is our answer.
