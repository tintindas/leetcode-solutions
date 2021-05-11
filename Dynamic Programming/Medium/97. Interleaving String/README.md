# 97. Interleaving String

## Problem Statement

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

```
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2+ s3 + t3 + ... or t1 + s1 + t2 + s2 +t3 + s3 + ...
```

Note: a + b is the concatenation of strings a and b.

## Solution Explained

We include one character from s1 or s2 and check whether the resultant string formed so far by one particular interleaving of the the current prefix of s1 and s2 form a prefix of s3.

Thus, this approach relies on the fact that the in order to determine whether a substring of s3(upto index k), can be formed by interleaving strings s1 and s2 upto indices i and j respectively, solely depends on the characters of s1 and s2 upto indices i and j only and not on the characters coming afterwards.
