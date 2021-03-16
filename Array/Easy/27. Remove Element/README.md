# 27. Remove Element

## Problem Statements

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## Main Concept

**Two Pointer Method** - Here we maintain two pointers at different indices of the array. This method is applicable to a lot of easy and medium difficulty array problems.

## Challenges

Loop termination condition - In this problem iterating through the entire list will not give us the solution instead we must iterate till i crosses j at which point we will have all the undesirable values at the end of the list and `i` will point to the last + 1 index of the answer array.

## Solution Explained

We initialise two pointers:

- `i = 0`, at the starting index of the array.
- `j = len(nums) - 1`, at the ending index of the array.

### Algorithm

- Everytime we see the element to be removed we swap the element at `j` with the element at `i`.
- We decrement `j` after every swap operation.
- When we see any element other than the one to be removed we increment `i`.
- We terminate the loop once `i` crosses `j`.

`i` gives us the length of the new array.
