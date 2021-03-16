# 35. Search Insert Position

## Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## Main Concept

**Binary Search** - Any time sorted array and search occur in the same sentence think Binary Search.

## Solution Explained

A basic binary search is implemented to search for the target value.

`mid = (lo + hi)//2` is calculated.

- If `mid` is equal to the `target` value we have our answer i.e. `mid`.
- If `target` is less than mid we discard the right half of the search space.
- If `target` is greater than mid we discard the left half of the search space.

The loop is terminated once `lo` crosses `hi`

We return `lo` if the `target` element is not found during the search.
