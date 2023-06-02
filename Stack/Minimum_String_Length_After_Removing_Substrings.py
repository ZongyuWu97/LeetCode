class Solution:
    def minLength(self, s: str) -> int:
        memo = {'D':'C', 'B':'A'}
        stack = []
        for ch in s:
            if stack and ch in memo and memo[ch] == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)