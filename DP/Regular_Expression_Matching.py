class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        m, n = len(s), len(p)

        def dp(i, j):
            if not (i, j) in memo:
                if j == n:
                    ans = i == m
                else:
                    first_match = i < m and p[j] in {s[i], "."}
                    if j < n - 1 and p[j + 1] == "*":
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
