class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)

        def dfs(sets, currSet, idx):
            if idx == n:
                return
            take = currSet + [nums[idx]]
            res.append(currSet + [nums[idx]])
            dfs(sets, take, idx + 1)
            dfs(sets, currSet, idx + 1)

        dfs(res, [], 0)
        return res
