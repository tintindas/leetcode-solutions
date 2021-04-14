# 234. Palindrome Linked List

## Problem Statement

Given the head of a singly linked list, return true if it is a palindrome.

## Solution Explained

In this solution we leverage two previously used solutions to different problems.

We first use the slow and fast pointer method to find the middle of the given linked list.

After the middle is found we reverse the second half of the linked list using the solution of [206. Reverse Linked List](../206.%20Reverse%20Linked%20List)

Then we traverse the two half lists looking for a difference. If one is found we return `False`. If both lists contain the same elements in same order then we return `True`.
