class Solution:
    def minimizedStringLength(self, s: str) -> int:
        memo = Counter(s)
        return len(memo)