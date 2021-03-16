# 1. Two Sum

## Problem Statement

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Main Concept

**Use of Hash Maps** - We can easily solve this problem by making use of Hash Maps which give us O(1) look up.

## Challenges

A one pass solution may not be apparent at first. Calculating the complement of each element in the array will give us the required solution.

## Solution Explained

We declare a dictionary `s` which will be used to map the elements in the array to their indices.

For every element in `nums` we calculate its complement i.e. `target - nums[i]`. We check if the complement already exists in `s` if it does not we add the element to `s`. If the complement does exist in `s` we return the index of the current element and the index of the complement.
