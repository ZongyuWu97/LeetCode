class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(nums, i):
            if i < 0:
                return False
            if not nums:
                if i == 0:
                    return True
                return False
            
            curr = 0
            m = len(nums)
            for j in range(m):
                curr = curr * 10 + nums[j]
                if dfs(nums[j + 1:], i - curr):
                    return True
            return False
            
        res = 0
        for i in range(1, n + 1):
            sqr = i * i
            nums = list(map(int, list(str(sqr))))
            if dfs(nums, i):
                res += sqr
        return res