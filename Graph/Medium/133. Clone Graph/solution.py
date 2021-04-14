from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node, visited):
        if not node:
            return

        if node in visited:
            return

        new_node = Node(node.val)
        self.m[node] = new_node
        visited[node] = True

        for u in node.neighbors:
            self.dfs(u, visited)

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        visited = defaultdict()
        self.m = defaultdict()
        self.dfs(node, visited)

        for k, v in self.m.items():
            v.neighbors = []
            if k.neighbors:
                for u in k.neighbors:
                    v.neighbors.append(self.m[u])

        return self.m[node]
