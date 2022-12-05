from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        cumu_sum = defaultdict(int)
        curr = 0
        cumu_sum[0] = 1
        for num in nums:
            curr += num
            count += cumu_sum[curr - k]
            cumu_sum[curr] += 1
        return count
