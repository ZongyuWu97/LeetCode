from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        res = float('inf')
        S = SortedList()
        for i in range(len(nums)):
            j = S.bisect_left(nums[i])
            # two options from here on
            # nums[i] - S[j-1]
            # S[j] - nums[i]
            if j < len(S):
                res = min(res, abs(S[j]-nums[i]))
            if j > 0:
                res = min(res, abs(S[j-1]-nums[i]))
            if i >= x-1:
                S.add(nums[i-(x-1)])
        return res