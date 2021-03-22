# 844. Backspace String Compare

## Problem Statement

Given two strings S and T, return if they are equal when both are typed into empty text editors. `#` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

## Solution Explained

We make a function to build the string as specified by the question.

We process the given string one element at a time. When we come across anything except for `#` we push it to the stack. If we come across a `#` we pop an element from the stack. We return a string constructed from the elements of the stack.

We invoke the function for the two input strings and then check if both our results are equal.
