class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        window = 0
        res = n + 1
        while r < n:
            window += nums[r]
            while window >= target:
                res = min(res, r - l + 1)
                window -= nums[l]
                l += 1
            r += 1
        return res if res <=n else 0