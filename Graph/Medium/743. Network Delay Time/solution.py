from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, node, graph, dist, time):
        if time >= dist[node]:
            return
        dist[node] = time
        for t, nei in sorted(graph[node]):
            self.dfs(nei, graph, dist, time + t)

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float("inf") for node in range(1, n + 1)}

        self.dfs(k, graph, dist, 0)
        ans = max(dist.values())
        return ans if ans < float("inf") else -1
