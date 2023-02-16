class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for idx, h in enumerate(heights):
            while stack and h >= heights[stack[-1]]:
                stack.pop()
            stack.append(idx)
        return stack
