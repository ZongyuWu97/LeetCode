class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = int(nums[0] == 1)
        prev = -1 if nums[0] == 0 else 0
        MOD = 10 ** 9 + 7
        
        for i in range(1, n):
            if nums[i] == 0:
                dp[i] = dp[i - 1]
                continue
            
            if prev == -1:
                dp[i] = 1
                prev = i
                continue
            
            dp[i] = sum(dp[prev:i]) % MOD
            prev = i
        print(dp)
        return dp[-1]
            
            