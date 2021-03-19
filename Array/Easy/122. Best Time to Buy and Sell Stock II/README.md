# 122. Best Time Buy and Sell Stock II

## Problem Statement

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Main Concept

**Traversing arrays** - This question asks for us to traverse the array one element at a time looking for consecutive valleys and peaks.

## Solution Explained

The solution is a straightforward traversal of the array.

We look for the first valley in the array. Once found, we look for a peak.

`max_profit = max_profit + peak - valley`, we do this calculation for each pair peak-value pair.

The process is repeated till the entire array is processed.
