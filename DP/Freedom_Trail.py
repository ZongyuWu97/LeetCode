class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring = list(ring)
        n = len(ring)
        dic = defaultdict(list)
        for i, ch in enumerate(ring):
            dic[ch].append(i)

        # form substring up to i-th in key, end at j-th in ring
        @lru_cache
        def dp(i, j):
            if i == 0:
                return min(j, n - j) + 1
            res = float("inf")
            for prev_idx in dic[key[i - 1]]:
                diff = abs(prev_idx - j)
                res = min(res, dp(i - 1, prev_idx) + min(diff, n - diff) + 1)
            return res

        return min([dp(len(key) - 1, j) for j in dic[key[-1]]])
