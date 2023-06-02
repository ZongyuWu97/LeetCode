class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    break
            
            if count < p:
                left = mid + 1
            else:
                right = mid
        return left