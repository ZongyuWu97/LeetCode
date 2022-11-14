class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])

            ans = jobDifficulty[i] + dfs(i+1, d-1)
            for j in range(i+2, n-d+2):
                ans = min(ans, max(jobDifficulty[i:j]) + dfs(j, d-1))
            return ans

        n = len(jobDifficulty)
        if n < d:
            return -1
        return dfs(0, d)
