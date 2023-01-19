class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float('inf')

        res = 0
        for price in prices:
            currMin = min(currMin, price)
            res = max(res, price - currMin)
        return res
