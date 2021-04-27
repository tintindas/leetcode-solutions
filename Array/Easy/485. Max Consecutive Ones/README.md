# 485. Max Consecutive Ones

## Problem Statement

Given a binary array nums, return the maximum number of consecutive 1's in the array.

## Solution Explained

We count the consecutive ones in the array. When we see a zero we reset our count to zero. We keep a track of our max count and return it after the loop.
