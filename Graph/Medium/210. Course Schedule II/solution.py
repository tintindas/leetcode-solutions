from typing import List


class Solution:
    def dfs(self, node, graph, visited, stack, ans):
        if node in stack:
            return -1

        if visited[node]:
            return

        stack.add(node)
        visited[node] = True
        for neighbour in graph[node]:
            if self.dfs(neighbour, graph, visited, stack, ans) == -1:
                return -1
        stack.remove(node)
        ans.append(node)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = []

        for _ in range(numCourses):
            graph.append([])

        for u, v in prerequisites:
            graph[v].append(u)

        visited = [False] * numCourses
        stack = set()
        ans = []

        for i in range(numCourses):
            if self.dfs(i, graph, visited, stack, ans) == -1:
                return []

        return ans[::-1]
