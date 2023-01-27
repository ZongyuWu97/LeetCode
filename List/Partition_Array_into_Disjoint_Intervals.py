class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        maxUntil = [0] * n
        minFrom = [0] * n

        currMax = nums[0]
        currMin = nums[-1]
        for i in range(n):
            currMax = max(currMax, nums[i])
            currMin = min(currMin, nums[-1 - i])
            maxUntil[i] = currMax
            minFrom[-1 - i] = currMin

        res = -1
        for i in range(n - 1):
            if maxUntil[i] <= minFrom[i + 1]:
                res = i
                break

        return res + 1
