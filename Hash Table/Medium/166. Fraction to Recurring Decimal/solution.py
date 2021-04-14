class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        ans = ""

        if numerator * denominator < 0:
            ans += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        q = numerator // denominator
        r = numerator % denominator

        ans += str(q)

        if r == 0:
            return ans

        ans += "."
        seen = {}

        while r != 0:
            if r in seen:
                ans = ans[: seen[r]] + "(" + ans[seen[r] :] + ")"
                break

            seen[r] = len(ans)

            r *= 10
            q = r // denominator
            r = r % denominator
            ans += str(q)

        return ans