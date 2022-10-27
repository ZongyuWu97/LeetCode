class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)

        @cache
        def dfs(i, j):
            if i == j:
                return 0
            elif i == j-1:
                return s[i] != s[j]

            if s[i] == s[j]:
                return dfs(i+1, j-1)
            else:
                return 1+min(dfs(i+1, j), dfs(i, j-1))
        return dfs(0, n-1) <= k