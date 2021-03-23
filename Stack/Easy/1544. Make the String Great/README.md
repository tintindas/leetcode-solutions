# 1544. Make the String Great

## Problem Statement

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

- 0 <= i <= s.length - 2
- s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

## Solution Explained

This solution is similar to the one in [1047. Remove all Adjacent Duplicates](https://github.com/tintindas/leetcode-solutions/tree/main/Stack/Easy/1047.%20Remove%20all%20Adjacent%20Duplicates%20from%20String).

We are just making extra checks for the cases of the letters. If the letter is lowercase we check whether the top of the stack is the uppercase of the letter and vice versa.
