class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        j = 0
        for i in range(n):
            stack.append(pushed[i])
            while j < n and stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        return stack == []