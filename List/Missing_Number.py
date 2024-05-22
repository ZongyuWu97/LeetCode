class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0] * (n + 1)
        for num in nums:
            l[num] = 1

        for i in range(n + 1):
            if l[i] == 0:
                return i
