# 166. Fraction to Recurring Decimal

## Problem Statement

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

## Solution Explained

First, we determine if our answer will be negative or not. If it will be negative we add a `-` to our answer.

We take the absolute values of the numerator and denominator. This is to deal with how negative division is handled in programming languages i.e. your answer will be one bigger than the real answer if you don't do this step.

We proceed as in regular division.

We take the quotient and add it to the answer. Then we check if the remainder is zero. If it is zero, we return the answer string.

If the remainder is not zero we enter in to a while loop.

While the remainder is not zero:

- Check if the remainder has been seen before.
- If it has been seen before we add brackets to the repeating part of the answer and break out of the loop.
- If it has not been seen before we add the length of the current answer string to our set. This is the index of the position where we will put the brackets if this remainder repeats.
- Then we do the normal division procedure i.e. we multiply the current remainder with 10. Get the quotient by dividing by the denominator and the new remaninder by taking modulo of remainder with denominator and then add the quotient to our answer string.

We return the answer string if the loop terminates.
