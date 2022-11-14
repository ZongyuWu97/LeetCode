class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        @lru_cache
        def isPalindrome(i, j):
            return s[i:j] == s[i:j][::-1]

        n = len(s)
        # 到i之前的长度至少k的回文串个数
        dp = [0] * (n + 1)
        dp[k] = int(isPalindrome(0, k))
        for i in range(k + 1, n + 1):
            curr_max = 0
            for j in range(i - k - 1, i - k + 1):
                curr_max = max(curr_max, dp[j] + isPalindrome(j, i))
            dp[i] = max(curr_max, dp[i - 1])
        return dp[-1]
