# 11. Container With Most Water

## Problem Statement

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

## Solution Explained

We initialise two pointers `left` and `right` at index 0 and last index of the array.

While our left pointer is less than our right pointer we calculate the area with the left and right pointers as the boundary. We keep a track of the maximum area we have seen.

We move the pointer which has lesser height to inward on every iteration.
