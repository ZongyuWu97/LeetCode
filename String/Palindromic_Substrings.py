class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n:
                if s[i + j] == s[i - j]:
                    count += 1
                    j += 1
                else:
                    break

            j = 0
            while i - j >= 0 and i + 1 + j < n:
                if s[i - j] == s[i + 1 + j]:
                    count += 1
                    j += 1
                else:
                    break
        return count
