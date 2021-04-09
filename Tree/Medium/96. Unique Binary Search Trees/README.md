# 96. Unique Binary Search Trees

## Problem Statement

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

## Main Concept

**Catalan Numbers** - The question is basically asking us to generate the nth catalan number

The formula for the nth catalan number is:

![Catalan Number formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/88d30f2a2c16ef8d6fbacb2647238cde5dd35cc3)

## Solution Explained

We use dynamic programming in this solution as the solution of the main problem depends on the soutions to its subproblems.

We initialise a dp array with the values [1,1] as, C<sub>0</sub> = 1 and C<sub>1</sub> = 1.

Then for 2 to n we run a loop which calculates,

![Catalan Number formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/88d30f2a2c16ef8d6fbacb2647238cde5dd35cc3)

in a inner loop.

We return the nth element of our dp array as our answer.
