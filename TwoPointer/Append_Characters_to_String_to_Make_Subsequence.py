class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        p = 0
        for ch in s:
            if p == n:
                return 0
            if ch == t[p]:
                p += 1
        return n - p