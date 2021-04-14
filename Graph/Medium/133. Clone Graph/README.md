# 133. Clone Graph

## Problem Statement

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

```python
class Node {
    public int val;
    public List<Node> neighbors;
}
```

## Solution Explained

We initialise a dictionary which maps our original nodes to their clones

We do a dfs traversal of the graph to reach all the nodes.

For each node we process we create its clone and then map the original node to the clone.

After we have all the nodes of our graph in the dictionary, for each pair of original and clone nodes we iterate over the neighbours of the original node and populate the adjacency list of the clone node with the nodes which are mapped to by the neighbours of the original node in our dictionary.
