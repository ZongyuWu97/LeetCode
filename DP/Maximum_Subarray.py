class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curr = res
        for num in nums:
            curr = max(num, curr + num)
            res = max(res, curr)
        return res
