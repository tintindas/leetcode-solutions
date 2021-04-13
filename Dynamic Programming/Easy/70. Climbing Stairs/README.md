# 70. Climbing Stairs

## Problem Statement

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Solution Explained

There are two ways to get to the kth step either you're coming from k-1th step or kth step.

Therefore the formula for number of ways to get to the kth step is:

`f(k) = f(k-1) + f(k-2)`

We keep a track of the number of ways we can get to the last two steps and build up our answer to the nth step.

Our base cases are:

```
f(0) = 1
f(1) = 1
```
