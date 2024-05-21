class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        n = len(nums)

        def dfs(prevXOR, idx):
            if idx == n:
                self.res += prevXOR
                return
            dfs(prevXOR ^ nums[idx], idx + 1)
            dfs(prevXOR, idx + 1)

        dfs(0, 0)
        return self.res
