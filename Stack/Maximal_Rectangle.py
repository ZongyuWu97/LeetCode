class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        hist = [[0] * n for _ in range(m)]
        for i in range(m):
            hist[i][0] = int(matrix[i][0] == '1')
            for j in range(1, n):
                hist[i][j] = (hist[i][j - 1] + 1) * (matrix[i][j] == '1')

        tmp = [0] * m
        res = 0
        for j in range(n):
            for i in range(m):
                tmp[i] = hist[i][j]
            res = max(res, self.largestRectangleArea(tmp))
        return res

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
