class Solution:
    @staticmethod
    def buildString(s: str):
        stack = []

        for c in s:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    def backspaceCompare(self, S: str, T: str) -> bool:

        s = self.buildString(S)
        t = self.buildString(T)

        return s == t
