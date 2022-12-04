from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        def clean(i):
            if window[0][0] <= i - k:
                window.popleft()
            while window and curr > window[-1][1]:
                window.pop()

        n = len(nums)
        window = deque()
        window.append([0, nums[0]])
        for i in range(1, n):
            # print(window)
            curr = window[0][1] + nums[i]
            clean(i)
            window.append((i, curr))
        return window[-1][1]
