class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)

        minFrom = [0] * n
        currMin = float('inf')
        for i in range(n - 1, -1, -1):
            currMin = min(currMin, nums[i])
            minFrom[i] = currMin

        prevMax = nums[0]
        res = 0

        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1

                if prevMax < nums[i] < minFrom[i + 1]:
                    res += 1

            prevMax = max(prevMax, nums[i])

        return res
