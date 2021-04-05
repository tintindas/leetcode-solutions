# 136. Single Number

## Problem Statement

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

**Follow up**: Could you implement a solution with a linear runtime complexity and without using extra memory?

## Solution Explained

The xor `^` operator can be used to solve this problem. Anything xored with zero is itself and anything xored with itself is zero.

```
0 ^ 4 = 4

3 ^ 3 = 0
```

Therefore, we can xor all the elements of the given list together and only the number which has a single copy will remain as the answer and the rest of the elements will xor with their pairs and become zero.
