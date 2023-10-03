class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        pos = {a: i for i, a in enumerate(nums)}
        res = n = len(nums)
        nums.sort()
        for i in range(1, n):
            if pos[nums[i]] < pos[nums[i - 1]]:
                res += n - i
        return res        