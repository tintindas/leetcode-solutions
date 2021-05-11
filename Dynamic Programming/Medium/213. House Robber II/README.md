# 213. House Robber II

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Solution Explained

Similar to [198. House Robber](../198.%20House%20Robber).

We consider the circular list as two lists one starting from the first house and ending at the last but one house and another starting at the second house and ending at the last house. Thus the first and the last house are not considered together. We return the maximum of the two return values.
