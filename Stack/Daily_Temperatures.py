class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for day, tem in enumerate(temperatures):
            while stack and tem > stack[-1][1]:
                idx = stack.pop()[0]
                ans[idx] = day - idx
            stack.append((day, tem))
        return ans
