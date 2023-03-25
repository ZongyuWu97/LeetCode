class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLength = 0
        left, right = 0, 0
        for i in range(n):
            l = 1
            while i + l <= n - 1 and i - l >= 0:
                if s[i + l] == s[i - l]:
                    l += 1
                else:
                     break
            if 2 * (l - 1) + 1 > maxLength:
                maxLength =  2 * (l - 1) + 1
                left, right = i - (l - 1), i + (l - 1)
            
            if i + 1 <= n - 1:
                l = 0
                while i + 1 + l <= n - 1 and i - l >= 0:
                    if s[i + 1 + l] == s[i - l]:
                        l += 1
                    else:
                        break
                if 2 * l > maxLength:
                    maxLength = 2 * l
                    left, right = i - (l - 1), i + 1 + (l - 1)
        return s[left: right + 1]