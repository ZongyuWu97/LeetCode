class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        start = s[n // 2] if n % 2 else ''
        string = []
        for i in range((n + 1) // 2, n):
            string.append(min(s[i], s[n - i - 1]))
        
        res = start
        for ch in string:
            res = ch + res + ch
        return res