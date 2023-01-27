class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i] = min cost for nums[:i]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # costs[s, t] = cost for nums[s:t + 1]
        costs = [[0] * (n) for _ in range(n)]
        for s in range(n):
            costs[s][s] = k
            tmp = {nums[s]: 1}
            for t in range(s + 1, n):
                curr = costs[s][t - 1]
                if not nums[t] in tmp:
                    tmp[nums[t]] = 1
                elif tmp[nums[t]] == 1:
                    tmp[nums[t]] += 1
                    curr += 2
                else:
                    tmp[nums[t]] += 1
                    curr += 1
                costs[s][t] = curr

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = min(dp[i], costs[j][i - 1] + dp[j])
        return dp[-1]
