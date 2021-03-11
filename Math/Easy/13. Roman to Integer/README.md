# 13. Roman to Integer

## Problem Statement

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| X      | 10    |
| L      | 50    |
| V      | 5     |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Main Concept

**Use of dictionaries** - This question mostly tests ones ability to not write a large number of if/else or switch statements. It is basic test of whether a data structure occurs to the test taker while solving interview problems.

## Challenges

1. Maintaining value mappings from Roman characters to their corresponding integer values. Did this via dictionaries.

2. Not writing a boat load of if/else or switch statements.

3. Handling the subtraction cases such as IV, XC, CD etc.

## Solution Explained

Use dictionaries to keep track of value mappings.

Iterate through the given string and add the value of the current character to the answer.

For cases such as IV, XC, CD etc. subtract twice the amount of the preceding numeral i.e. I, X, C etc. when the value of the current character is greater than the value of the preceding character. This can be done without issue because Roman numerals are written in order of decreasing value except for the subtraction cases which we are handling.

### Example

XIV

```
# Dry Run

ans = 0

# First iteration
1. X = 10
   ans = 10

# Second iteration
2. I = 1
   ans = 10 + 1 = 11

# Third iteration
3. V = 5
   ans = 11 + 5 = 16
   V > I
   ans = 16 - 2*1 = 16 - 2 = 14
```
