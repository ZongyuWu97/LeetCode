class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        left = 0
        n = len(s)
        res = 0

        for i in range(n):
            if s[i] in memo and memo[s[i]] >= left:
                left = memo[s[i]] + 1
            memo[s[i]] = i
            res = max(res, i - left + 1)
        
        return res