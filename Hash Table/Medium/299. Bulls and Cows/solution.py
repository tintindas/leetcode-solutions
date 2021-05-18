from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls = cows = 0
        other = []
        d = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                d[secret[i]] += 1
                other.append(guess[i])

        for c in other:
            if c in d:
                cows += 1
                d[c] -= 1
                if d[c] == 0:
                    d.pop(c)

        return f"{bulls}A{cows}B"