from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        for num in nums:
            prev = k - num
            if count[prev] > 0:
                count[prev] -= 1
                res += 1
            else:
                count[num] += 1
        return res
