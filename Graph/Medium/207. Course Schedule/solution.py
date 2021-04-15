from typing import List


class Solution:
    def has_cycle(self, node, graph, visited):
        if visited[node] == 1:
            return False

        if visited[node] == -1:
            return True

        visited[node] = -1

        for neighbour in graph[node]:
            if self.has_cycle(neighbour, graph, visited):
                return True

        visited[node] = 1
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []

        for _ in range(numCourses):
            graph.append([])

        for u, v in prerequisites:
            graph[u].append(v)

        visited = [0] * numCourses
        for i in range(numCourses):
            if self.has_cycle(i, graph, visited):
                return False

        return True