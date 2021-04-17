# 743. Network Delay Time

## Problem Statement

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

## Solution Explained

We do a dfs traversal and keep a track of the time it takes to get each node from the source node.

Instead of a visited array we have a distance array. If we reach a node we have seen before in our dfs traversal we still it visit it if our current path takes less time to get to the node than previously. This way we get the minimum time to get to every node in the graph from the source node.

Our answer is the maximum time taken to get to a node. If a node is not reached ever it has infinite time so we return -1.
