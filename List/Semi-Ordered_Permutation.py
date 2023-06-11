import bisect
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        for idx, num in enumerate(nums):
            if num == 1:
                i1 = idx
            if num == n:
                iN = idx

        return i1 + (n - iN - 1) - int(i1 > iN)