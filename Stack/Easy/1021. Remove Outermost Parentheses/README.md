# 1021. Remove Outermost Parentheses

## Problem Statement

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation. For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

## Main Concept

**Levels** - In this question we have to keep track of how many levels deep we are into the parentheses string.

## Solution Explained

We initialise `start = 0` to keep a track of the start of our outermost parentheses.
`Level` keeps track of how many levels deep we are within the parentheses string. `res` will be the final return string.

We process the given input string:

- if '(' is encountered we add `1` to `level`.
- if ')' is encountered we subtract `1` from `level`.

When `level` becomes `0` we have processed one pair of outermost parentheses. Thus we add everything within these parentheses i.e. from `start+1` to the index being processed to our result string.

We set `start` as `i+1` to mark the beginning of another pair of outermost parentheses.

`res` is the desired string.
