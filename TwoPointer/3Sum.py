class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i == 0 or nums[i - 1] != nums[i]:
                tmp = {}
                target = -nums[i]
                left, right = i + 1, n - 1
                while left < right:
                    curr = nums[left] + nums[right]
                    if curr < target:
                        left += 1
                    elif curr > target:
                        right -= 1
                    else:
                        res.add((nums[i], nums[left], nums[right]))
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return list(res)
