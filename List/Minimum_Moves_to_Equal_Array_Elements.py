class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        ans = 0
        for num in nums:
            ans += num - m
        return ans
