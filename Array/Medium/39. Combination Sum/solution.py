from typing import List


class Solution:
    def helper(self, candidates, path, target, idx):
        if target < 0 or idx > len(candidates) - 1:
            return

        if target == 0:
            self.res.append(path)
            return

        self.helper(candidates, path, target, idx + 1)
        self.helper(candidates, path + [candidates[idx]], target - candidates[idx], idx)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        self.res = []
        self.helper(candidates, [], target, 0)
        return self.res