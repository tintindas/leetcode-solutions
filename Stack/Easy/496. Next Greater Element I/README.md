# 496. Next Greater Element I

## Problem Statement

You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.

## Challenges

Understanding the question - Sometimes questions on leetcode and even real interviews are badly formulated. Ask a ton of questions if a question like this shows up in a real interview.

## Solution Explained

The question asks us to look at a number in `nums1`, find it in `nums2` and then find its next greatest number to the right in `nums2`.

We initialise an empty dictionary and stack.

We put the first element of `nums2` in the stack.

For the elements in `nums2` we check if they are greater than the numbers on their left. We do this by checking the numbers in the stack. The stack contains all the elements of `nums2` for which we haven't found a greater element to its right. The number being processed becomes the next greater number for every element in the stack to which it is greater. We pop every element off the stack for which a greater element has been found to the right.

If after we have processed all the elements in `nums2` there are still some elements left in the stack we map all those elements to `-1`.

Then we just return the mappings of every element we encounter in `nums1`.
