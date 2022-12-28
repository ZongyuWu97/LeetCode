class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = set()
        for i in range(n - 3):
            if i == 0 or nums[i - 1] != nums[i]:
                for j in range(i + 1, n - 2):
                    if j == i + 1 or nums[j - 1] != nums[j]:
                        left, right = j + 1, n - 1
                        curr_target = target - nums[i] - nums[j]
                        while left < right:
                            curr_sum = nums[left] + nums[right]
                            if curr_sum < curr_target:
                                left += 1
                            elif curr_sum > curr_target:
                                right -= 1
                            else:
                                res.add(
                                    (nums[i], nums[j], nums[left], nums[right]))
                                left += 1
                                right -= 1

        return list(res)
