from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def clean(i):
            if window and window[0] == i - k:
                window.popleft()
            while window and nums[i] > nums[window[-1]]:
                window.pop()

        if k == 1:
            return nums
        n = len(nums)

        window = deque()
        max_idx = 0
        for i in range(k):
            clean(i)
            window.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        ans = [nums[max_idx]]

        for i in range(k, n):
            clean(i)
            window.append(i)
            ans.append(nums[window[0]])

        return ans
