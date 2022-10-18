class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def helper(target):
            count = 0
            if target == 0:
                return 1
            elif target < 0:
                return 0

            for num in nums:
                count += helper(target-num)

            return count
        return helper(target)
