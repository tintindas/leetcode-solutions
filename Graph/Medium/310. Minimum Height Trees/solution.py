from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]

        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = []

        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            temp = []

            for leaf in leaves:
                for neighbour in graph[leaf]:
                    graph[neighbour].remove(leaf)
                    if len(graph[neighbour]) == 1:
                        temp.append(neighbour)
            leaves = temp

        return leaves
