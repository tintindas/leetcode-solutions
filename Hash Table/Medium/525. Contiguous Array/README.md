# 525. Contiguous Array

## Problem Statement

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

## Solution Explained

We make use of a count variable, which is used to store the relative number of ones and zeros encountered so far while traversing the array. The count variable is incremented by one for every `1` encountered and the same is decremented by one for every `0` encountered.

We start traversing the array from the beginning. If at any moment, the count becomes zero, it implies that we've encountered equal number of zeros and ones from the beginning till the current index of the array(iii). Not only this, another point to be noted is that if we encounter the same count twice while traversing the array, it means that the number of zeros and ones are equal between the indices corresponding to the equal count values.
