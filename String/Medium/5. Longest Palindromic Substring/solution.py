class Solution:
    def helper(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        return s[start + 1 : end]

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        ans = ""
        n = len(s)
        s1 = ""
        s2 = ""
        for i in range(n):
            s1 = self.helper(s, i, i)
            if i != n - 1:
                s2 = self.helper(s, i, i + 1)

            ans = s1 if len(s1) > len(ans) else ans
            ans = s2 if len(s2) > len(ans) else ans

        return ans
