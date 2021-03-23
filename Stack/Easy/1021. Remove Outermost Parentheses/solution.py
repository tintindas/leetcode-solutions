class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        res = ""
        level = 0
        start = 0

        for i, c in enumerate(S):
            if c == "(":
                level += 1
            if c == ")":
                level -= 1

            if level == 0:
                res += S[start + 1 : i]
                start = i + 1

        return res
