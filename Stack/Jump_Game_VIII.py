class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)

        # Use monostack to get the next greater and smaller index
        ngi, nsi = [n] * n, [n] * n
        minmono, maxmono = [], []
        for i in range(n):
            while minmono and nums[minmono[-1]] <= nums[i]:
                ngi[minmono.pop()] = i
            while maxmono and nums[maxmono[-1]] > nums[i]:
                nsi[maxmono.pop()] = i
            
            minmono.append(i)
            maxmono.append(i)
        
        # DP for result
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            for idx in ngi[i], nsi[i]:
                if idx < n:
                    dp[idx] = min(dp[idx], dp[i] + costs[idx])
        return dp[-1]
