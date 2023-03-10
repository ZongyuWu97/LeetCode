class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0

        for j in range((n + 1) // 2, n):
            if 2 * nums[i] <= nums[j]:
                i += 1
        return 2 * i
