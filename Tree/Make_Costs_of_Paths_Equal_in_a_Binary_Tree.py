class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = i * 2 + 1, i * 2 + 2
            res += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])
        return res