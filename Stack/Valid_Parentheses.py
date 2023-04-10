class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'}':'{', ']': '[', ')': '('}
        for ch in s:
            if not ch in parentheses:
                stack.append(ch)
                continue
            if stack and parentheses[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False