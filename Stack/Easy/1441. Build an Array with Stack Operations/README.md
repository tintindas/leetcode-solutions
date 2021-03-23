# 1441. Build an Array with Stack Operations

## Problem Statement

Given an array target and an integer n. In each iteration, you will read a number from list = {1,2,3..., n}.

Build the target array using the following operations:

- Push: Read a new element from the beginning list, and push it in the array.
- Pop: delete the last element of the array.
- If the target array is already built, stop reading more elements.

Return the operations to build the target array. You are guaranteed that the answer is unique.

## Solution Explained

We have to recreate the target array given to us with `Push` and `Pop` operations.

Our solution places a pointer at the start of the `target` array. Then we look through the list [1, n], the current element of the list is marked by `j`.

Now there can only be two situatuons either the number at index `i` matches the number `j` or it does not.

If there is a match we need only to do a `Push` operation and increment `i`, thereby marking the current element of `target` as processed.

If we do not have a match then we must do a `Push` followed by a `Pop`. `i` is not incremented as we have not yet seen the `i`th element of `target` in the list.

We increment `j` in every iteration.
