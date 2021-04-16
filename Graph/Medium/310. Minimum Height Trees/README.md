# 310. Minimum Height Trees

## Problem Statement

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h)) are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

## Solution Explained

The main idea to solve this problem is to understand that the root of the minimum height tree will be in the center of the graph.

First, we construct our graph.

Then we keep a track of our leaf nodes with an array.

While we have more than two nodes in our graph we keep removing the outermost layer of leaves from the graph.

When there is either only node left or two nodes left, they are our central nodes and root the minimum height trees. So we return an array of them.

## Notes

1. [Video Explanation](https://www.youtube.com/watch?v=ZfzVig8UqBQ)
