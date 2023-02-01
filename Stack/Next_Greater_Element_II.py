class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] = num
            stack.append(i)

        for num in nums:
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] = num

        return res
