# 263. Ugly Number

## Problem Statement

Given an integer n, return true if n is an ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.

## Main Concept

**Factors** - If a number is ugly it will be equal to one after we factorise all the 2's, 3's and 5's out.

## Challenges

Not writing too many if/else clauses.

## Solution Explained

We write a guard clause to take care of non-positive inputs.

Then we factorise out the 2's, 3's and 5's with three while loops.

If the remaining number is equal to 1 it is ugly.
