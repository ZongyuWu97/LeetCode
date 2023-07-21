class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        dp = [[-1] * (1 << n) for _ in range(k + 1)]

        def unfairness(k, bagMask):
            if dp[k][bagMask] != -1:
                return dp[k][bagMask]
            
            def sumMask(mask):
                res = 0
                for i in range(n):
                    if mask & (1 << i):
                        res += cookies[i]
                return res
            
            if k == 1:
                dp[k][bagMask] = sumMask(bagMask)
                return dp[k][bagMask]
            
            res = 2 ** 31
            mask = bagMask
            while mask > 0:
                sum1 = sumMask(mask)
                sum2 = unfairness(k - 1, bagMask ^ mask)
                mask = (mask - 1) & bagMask
                res = min(res, max(sum1, sum2))
            dp[k][bagMask] = res
            return res
        return unfairness(k, (1 << n) - 1)


