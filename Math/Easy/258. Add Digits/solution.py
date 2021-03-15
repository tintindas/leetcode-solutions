class Solution:
    @staticmethod
    def add_digits(n: int) -> int:
        res = 0
        while n:
            res += n % 10
            n //= 10
        return res

    def addDigits(self, num: int) -> int:
        while num // 10:
            num = Solution.add_digits(num)
        return num