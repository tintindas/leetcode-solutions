# 66. Plus One

## Problem Statement

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

## Solution Explained

1. Reverse the array.
2. Initialise `carry = 1`.
3. Now we process each number in the reversed array and add the carry to it.
4. The face value of the digit is `digit%10` and the carry is given by `digit//10`.
5. We break out of the loop if `carry = 0` or if all elements in the array have been processed.
6. If there is still a carry after the loop we append a `1` to the reversed list.
7. The reverse of the reversed list is returned as the answer.
