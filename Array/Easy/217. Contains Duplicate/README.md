# 217. Contains Duplicate

## Problem Statement

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Main Concept

**Use of Sets** - Sets are data structures where duplicates are not allowed.

## Solution Explained

We initialise a set with the given array as input.

If the length of set is equal to the length of the array then there are no duplicates. However, if the lenght of the set is less than the length of the array then the array must contain duplicates.
