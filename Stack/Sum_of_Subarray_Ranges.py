class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        rightLess = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                rightLess[stack.pop()] = i
            stack.append(i)

        leftLargeEqual = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                leftLargeEqual[stack.pop()] = i
            stack.append(i)

        rightLarge = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                rightLarge[stack.pop()] = i
            stack.append(i)

        leftLessEqual = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                leftLessEqual[stack.pop()] = i
            stack.append(i)

        ans = 0
        for i in range(n):
            ans += nums[i] * ((rightLarge[i] - i) * (i - leftLessEqual[i])
                              - (rightLess[i] - i) * (i - leftLargeEqual[i]))

        return ans
