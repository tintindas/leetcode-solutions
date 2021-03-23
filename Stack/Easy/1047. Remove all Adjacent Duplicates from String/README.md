# 1047. Remove All Adjacent Duplicates from String

## Problem Statement

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed the answer is unique.

## Solution Explained

This a simple stack question.

In our solution we just pop the top of the stack whenever the element being processed is the same as the top. If the element is not equal to the top of the stack it is pushed onto the stack. After all the characters of the string have been processed the resulting stack has all the characters of the required result in order.
