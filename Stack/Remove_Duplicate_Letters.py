class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {ch: idx for idx, ch in enumerate(s)}
        stack = []
        memo = set()

        for idx, ch in enumerate(s):
            if not ch in memo:
                while stack and stack[-1] > ch and last_occur[stack[-1]] > idx:
                    memo.remove(stack.pop())
                stack.append(ch)
                memo.add(ch)

        return ''.join(stack)
