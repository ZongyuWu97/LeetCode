class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        dp = [2] * n
        memo = {'c':set(['b', 'a']), 'b':set('a'), 'a':set()}

        for i in range(1, n):
            if word[i - 1] in memo[word[i]]:
                dp[i] = dp[i - 1] - 1
            else:
                dp[i] = dp[i - 1] + 2
        return dp[-1]
        