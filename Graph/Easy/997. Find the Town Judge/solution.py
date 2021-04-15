from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)

        for pair in trust:
            indegree[pair[1]] += 1
            outdegree[pair[0]] += 1

        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i

        return -1