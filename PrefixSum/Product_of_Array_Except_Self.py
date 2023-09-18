class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        tmp = 1
        for j in range(n - 2, -1, -1):
            tmp *= nums[j + 1]
            res[j] *= tmp
        return res
