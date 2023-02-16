class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if stack:
                curr_max = stack[-1]
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(max(curr_max, num))
            else:
                stack.append(num)
        return len(stack)
