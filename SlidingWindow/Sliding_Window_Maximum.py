from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def clean(i):
            if window and window[0] == i - k:
                window.popleft()
            while window and nums[i] >= nums[window[-1]]:
                window.pop()

        n = len(nums)
        window = deque()
        for i in range(k):
            clean(i)
            window.append(i)

        ans = [nums[window[0]]]
        for i in range(k, n):
            clean(i)
            window.append(i)
            ans.append(nums[window[0]])
        return ans
