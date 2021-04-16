# 399. Evaluate Division

## Problem Statement

numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

**Note**: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

## Solution Explained

We create an undirected graph where the edge from `u -> v` gives the result of `u/v`.

We then do a dfs traversal of the from the numerator to the denominator for every query.

In the dfs function:

- If either the numerator or denominator do not exist in the graph then an answer cannot exist.

- If the denominator is a neighbour of the numerator we return the edge from `num -> den`

- If the numerator and denominator are not immediate neighbours we do dfs traversal for all the neighbours.
