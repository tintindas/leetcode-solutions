# 26. Remove Duplicates from Sorted Array

## Problem Statement

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## Main Concept

**Two Pointer Method** - Here we maintain two pointers at different indices of the array. This method is applicable to a lot of easy and medium difficulty array problems.

## Solution Explained

Initialise two pointers `i = j = 1`

The pointer `i` denotes the position we can overwrite with a new number i.e. it is a duplicate.

The `j` pointer traverses through the array and every time it encounters a new number we overwrite the number at index `i` with the new number and then increment `i`.

We return `i` as the final answer after all elements of the array have been processed.
