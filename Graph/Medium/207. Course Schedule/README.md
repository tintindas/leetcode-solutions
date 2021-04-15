# 207. Course Schedule

## Problem Statement

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

## Solution Explained

We create an adjacency list representation of the graph whose edges we are given as input.

Now we do a simple dfs traversal of the graph. When we just visit a graph we mark it in the `visited` array as `-1` indicating that we have reached the node but we have not completed visiting it yet, i.e. it is in our recursion stack.

When we complete visiting the node we mark it as `1` in our `visited` array. Indicating that all dfs paths going through the node have been explored.

If we come across a node that is already in our recursion stack then we have encountered a cycle in our graph.

To satisfy the questions requirements our graph should be acyclic.
