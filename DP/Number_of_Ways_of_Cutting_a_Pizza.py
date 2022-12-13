class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        num_apples = [[0] * (n + 1) for _ in range(m + 1)]
        mod = 10**9 + 7

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                num_apples[i][j] = int(pizza[i][j] == 'A') +\
                    num_apples[i + 1][j] +\
                    num_apples[i][j + 1] -\
                    num_apples[i + 1][j + 1]

        @lru_cache(None)
        def num_ways(i, j, K):
            if K == 1:
                return 1
            if i == m or j == n:
                return 0

            res = 0
            for x in range(i + 1, m + 1):
                if num_apples[i][j] - num_apples[x][j] > 0 and num_apples[x][j] > 0:
                    res = (res + num_ways(x, j, K - 1)) % mod
            for y in range(j + 1, n + 1):
                if num_apples[i][j] - num_apples[i][y] > 0 and num_apples[i][y] > 0:
                    res = (res + num_ways(i, y, K - 1)) % mod
            return res

        return num_ways(0, 0, k)
