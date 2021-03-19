# 169. Majority Element

## Problem Statement

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

## Main Concept

**Use of HashMaps** - We use the Counter object in python to map the values in the array to their count and then return the element with the maximum count.

## Solution Explained

We initialise a Counter object with the given array as input.

We then return the element with maximum count as the answer.

## Notes

The `max` function in python can take an optinal `key` argument when given an iterable using which it will do the comparisons.

For example, for a dictionary rather than using the keys in the comparison it will use the return values if specified.
