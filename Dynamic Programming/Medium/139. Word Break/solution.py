from typing import List


class Solution:
    def helper(self, s, wordDict):
        if s in self.memo:
            return self.memo[s]

        if not s:
            return True

        for word in wordDict:
            if s.find(word) == 0:
                if self.helper(s[len(word) :], wordDict):
                    self.memo[s] = True
                    return True
        self.memo[s] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        return self.helper(s, wordDict)