class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        costs = [float('inf')] * n
        
        res = float('inf')
        for rotate in range(n):
            rotate_cost = x * rotate
            for i in range(n):
                costs[i] = min(costs[i], nums[i - rotate])
            res = min(res, sum(costs) + rotate_cost)
        return res