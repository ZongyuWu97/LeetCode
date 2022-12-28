
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [(-1, 0)]
        n = len(heights)
        for i in range(n):
            if heights[i] < stack[-1][1]:
                while stack[-1][1] > heights[i]:
                    _, height = stack.pop()
                    res = max(res, height * (i - stack[-1][0] - 1))
            stack.append((i, heights[i]))

        while stack[-1][1] != 0:
            _, height = stack.pop()
            res = max(res, height * (n - stack[-1][0] - 1))

        return res
