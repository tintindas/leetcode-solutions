class Solution:
    @staticmethod
    def calculate(n: int) -> int:
        res = 0
        for i in str(n):
            res += int(i) ** 2
        return res

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        s = set()

        while n != 1:
            n = Solution.calculate(n)
            if n in s:
                return False
            s.add(n)

        return True
