class Solution: 
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        memo = {}
        n = len(nums)
        
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j - i <= 1:
                memo[(i, j)] = True
            else:
                memo[(i, j)] = (sum(nums[i + 1:j + 1]) >= m and helper(i + 1, j))\
                            or (sum(nums[i:j]) >= m and helper(i, j - 1))
            return memo[(i, j)]
        return helper(0, n - 1)