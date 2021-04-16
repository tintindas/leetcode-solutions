# 210. Course Schedule II

## Problem Statement

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Main Concept

**Topological Sort** - A topological sort is sorting tasks by the order in which they must be done i.e. if 0 must be done before 1 then the order is [0, 1].

## Challenges

We must detect cycles in the graph. A topological sort is only possible in a directed acyclic graph.

## Solution Explained

We do a simple dfs traversal of the graph. Each element that is currently in the recursion stack is put in our `stack` set. When we are done processing the node we put it in our answer array and remove it from our `stack` set.

When we see a node which is already in our recursion stack we have encountered a cycle and return `-1` up our recursion calls. When the main function receives the `-1` it will return `[]` because no order is possible due to the cycle.
