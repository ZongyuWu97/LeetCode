class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def getCost(x):
            res = 0
            for i in range(n):
                res += abs(nums[i] - x) * cost[i]
            return res

        left = min(nums)
        right = max(nums)
        n = len(nums)

        while left < right:
            mid = (left + right) // 2
            if getCost(mid) < getCost(mid + 1):
                right = mid
            else:
                left = mid + 1
        return getCost(left)
