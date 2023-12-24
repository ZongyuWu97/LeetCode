class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        window = defaultdict(int)
        l, r = 0, 0
        n = len(nums)
        res = 0
        while r < n:
            curr += nums[r]
            window[nums[r]] += 1
            while r - l + 1 > k or window[nums[r]] > 1:
                curr -= nums[l]
                window[nums[l]] -= 1
                l += 1
            if r - l + 1 == k:
                res = max(res, curr)
            r += 1
        return res


