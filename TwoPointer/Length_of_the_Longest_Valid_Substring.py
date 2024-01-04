class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        forbiddenSet = set(forbidden)
        l = 0
        res = 0
        for r in range(1, n + 1):
            for k in range(r - 1, max(r - 10, l) - 1, -1):
                if word[k:r] in forbiddenSet:
                    l = k + 1
                    break
            res = max(res, r - l)
        return res
