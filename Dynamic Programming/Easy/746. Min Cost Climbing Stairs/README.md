# 746. Min Cost Climbing Stairs

## Problem Statement

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

## Solution Explained

This solution is very similar to [70. Climbing Stairs](../70.%20Climbing%20Stairs).

We just modified it to get the minimum cost from the given cost arrays on each iteration.

We also return the minimum cost to get to either the n-1th step or n-2th step.
