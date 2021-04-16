from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, num, den, visited, graph):
        if num not in graph or den not in graph:
            return -1.0

        if den in graph[num]:
            return graph[num][den]

        for i in graph[num]:
            if i not in visited:
                visited.add(i)
                temp = self.dfs(i, den, visited, graph)
                if temp == -1.0:
                    continue
                else:
                    return graph[num][i] * temp
        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        res = []
        for num, den in queries:
            visited = set()
            ans = self.dfs(num, den, visited, graph)
            res.append(ans)

        return res