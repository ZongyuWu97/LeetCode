class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        cnt = 0
        sum_l = nums[0]
        sum_r = nums[n - 1]

        while l < r:
            if sum_l == sum_r:
                l += 1
                r -= 1
                sum_l = nums[l]
                sum_r = nums[r]
            elif sum_l < sum_r:
                l += 1
                sum_l += nums[l]
                cnt += 1
            else:
                r -= 1
                sum_r += nums[r]
                cnt += 1
        return cnt
