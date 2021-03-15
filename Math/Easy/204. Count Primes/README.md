# 204. Count Primes

## Problem Statement

Count the number of prime numbers less than a non-negative number, _n_.

## Main Concept

**Sieve of Erastothenes** - The idea behind this algorithm is to make a list of every non-negative integer till n. Then mark the multiples of each prime number in the list as non-prime. This yields the prime numbers.

## Challenges

Finding a solution that works better than O(n^2).

## Solution Explained

We initialise an array assuming every number in it is prime.

Then for numbers from 2 to n, we mark the multiples of the numbers as not prime i.e. 0.

At the end of the loop we are left with only the primes marked as 1. Summing up the ones we get the number of primes under n.

## Notes

1. We can run the loop to sqrt(n). [Explanation here](https://math.stackexchange.com/a/58808).
