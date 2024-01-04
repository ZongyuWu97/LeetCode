from bisect import bisect_left
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pre, suf = [nums[0]] + [0] * (n - 1), [0] * (n - 1) + [nums[-1]]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
            suf[-i - 1] = suf[-i] + nums[-i - 1]

        res = []
        for q in queries:
            idx = bisect_left(nums, q)
            if idx <= 0:
                res.append(suf[0] - n * q)
            elif idx >= n - 1:
                res.append(n * q - pre[n - 1])
            else:
                res.append(q * (idx) - pre[idx - 1] + suf[idx] - q * (n - idx))
        return res