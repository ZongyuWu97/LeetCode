class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = nums[0]
        res = 1
        for num in nums:
            if num - m > k:
                m = num
                res += 1
        return res
