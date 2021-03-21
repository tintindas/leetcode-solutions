class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opposites = {')': '(', '}':'{', ']':'['}
        
        for c in s:
            if c in opposites:
                if not stack or stack[-1] != opposites[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
        