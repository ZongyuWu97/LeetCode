class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2):
            if n % (i + 1) == 0:
                if s == s[:i + 1] * (n // (i + 1)):
                    return True
        return False