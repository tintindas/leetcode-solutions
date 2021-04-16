from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, source, target, graph, visited):
        if source not in visited:
            visited.add(source)
            if source == target:
                return True
            for nei in graph[source]:
                if self.dfs(nei, target, graph, visited):
                    return True
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            visited = set()
            if u in graph and v in graph and self.dfs(u, v, graph, visited):
                return u, v
            graph[u].append(v)
            graph[v].append(u)