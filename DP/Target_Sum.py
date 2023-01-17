class Solution:
    def __init__(self):
        self.dp = collections.defaultdict(dict)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target in self.dp[n]:
            return self.dp[n][target]

        if n == 0:
            res = int(target == 0)
        else:
            res = self.findTargetSumWays(
                nums[:-1], target - nums[-1]) + self.findTargetSumWays(nums[:-1], target + nums[-1])

        self.dp[n][target] = res
        return res
