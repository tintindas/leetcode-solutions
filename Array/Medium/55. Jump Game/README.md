# 55. Jump Game

## Problem Statement

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

## Solution Explained

We initialise our destination as the last index of the array.

We start at the end of the array and iterate backwards. For each element we check if the reach from that position i.e. index of elements + element itself is greater than the destination. If it is, we update the destination to be the index of our current element. We do this because we have just verified that we can reach our destination from our current position. Now, we only need to know if we can reach the current index.

If at the end of the loop our destination is the first index of the array we return True.
