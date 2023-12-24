class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        groups = collections.defaultdict(set)
        for num in nums:
            groups[num % k].add(num)
        
        res = 1
        for group in groups:
            n = len(groups[group])
            curr = sorted(groups[group])
            if n == 1:
                res *= 2
            elif n == 2:
                res *= 3 + (curr[1] - k != curr[0])
            else:
                dp = [0] * n
                dp[0], dp[1] = 2, 3 + (curr[1] - k != curr[0])
                for i in range(2, n):
                    if curr[i] - k == curr[i - 1]:
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = 2 * dp[i - 1]
                res *= dp[-1]
        return res
