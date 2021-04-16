from collections import defaultdict
from bisect import insort
from typing import List


class Solution:
    def dfs(self, node, graph, stack):

        while graph[node]:
            next_dest = graph[node][0]
            graph[node].remove(next_dest)
            self.dfs(next_dest, graph, stack)

        stack.append(node)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dest in tickets:
            insort(graph[src], dest)

        stack = []

        self.dfs("JFK", graph, stack)

        return stack[::-1]