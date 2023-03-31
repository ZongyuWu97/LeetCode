class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)
        for i in range(n - 1):
            if (self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]))\
                or (self.isScramble(s1[:i + 1], s2[n - (i + 1):]) and self.isScramble(s1[i + 1:], s2[:n - (i + 1)])):
                return True
        return False