class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(1, 1)] * n # number of LIS, length of LIS
        for i in range(1, n):
            l = 1
            s = 1
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if dp[j][1] + 1 > l:
                    l, s = dp[j][1] + 1, dp[j][0]
                elif dp[j][1] + 1 == l:
                    s += dp[j][0]
            dp[i] = (s, l)
        
        l, s = 1, 0
        for i in range(n):
            if dp[i][1] > l:
                l, s = dp[i][1], dp[i][0]
            elif dp[i][1] == l:
                s += dp[i][0]
        # print(dp)
        return s
                    