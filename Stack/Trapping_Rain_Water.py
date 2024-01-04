class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                base = height[stack.pop()]
                if stack:
                    ans += (min(height[i], height[stack[-1]]) - base) * (i - stack[-1] - 1)
            stack.append(i)
        return ans