class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        res = -1
        m, M = min(nums), max(nums)
        for num in nums:
            if num != m and num != M:
                return num
        return -1