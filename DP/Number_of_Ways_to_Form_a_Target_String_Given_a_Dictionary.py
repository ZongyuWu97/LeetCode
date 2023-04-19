class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        count = {}
        for i in range(n):
            count[i] = Counter([word[i] for word in words])

        t = len(target)
        if n < t:
            return 0

        MOD = 10 ** 9 + 7

        @cache
        def dp(t, n):
            if t == 1:
                return sum([count[i][target[0]] for i in range(n)])
            res = 0
            for i in range(t - 1, n):
                res += dp(t - 1, i) * count[i][target[t - 1]]
                res %= MOD
            # print(t, n, res)
            return res

        return dp(t, n)