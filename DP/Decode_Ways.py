class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i):
            # Number of ways for s[i:]
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if i == n - 1:
                return 1
            return dp(i + 1) + int(int(s[i : i + 2]) < 27) * dp(i + 2)

        return dp(0)
