# 274. H-Index

## Problem Statement

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

## Main Concept

**Sorting** - The citations list has to be sorted in descending order to make this questions easy.

## Solution Explained

We sort the list in descending order.

Now finding the answer is a simple job of scanning the list till we find the element which is smaller than its `index + 1` (as python lists are zero-indexed).

Once found either the element itself will be the answer i.e. the element at `hth` index will have exacty `h` citations or the answer will the index we are processing i.e. `i` because the element has less than `i+1` citations.

We can safely determine the above to be true because the list is sorted in descending order. Everything to the left of the first violation of `citations[i] <= i+1` must by definition satisfy the condition of having more citations than its index value and everything to the right of the sorted list must violate the condition.
