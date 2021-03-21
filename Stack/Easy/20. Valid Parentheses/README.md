# 20. Valid Parentheses

## Problem Statement

Given a string s containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
1. Open brackets must be closed in the correct order.

## Main Concept

**Stacks** - A stack is a first-in-last-out data structure. It is especially useful for keeping track of the most recently inserted elements.

## Solution Explained

- We initialise an empty stack.
- We process the array one element at a time.
  - If the element is an opening bracket it is inserted into the stack.
  - When a closing bracket is encountered we check if the top element of the stack corresponds to the encountered closing bracket. If it does we pop the top from the stack, thereby pairing off one pair of brackets. If it does not we return `False`, as it is not a valid string. Before checking for the top element of the stack we must check if the stack is not empty. An empty stack with only a closing bracket will always be invalid.
- After our entire string has been processed we should have an empty stack in case of a valid string as all brackets will have been paired off in the loop.
