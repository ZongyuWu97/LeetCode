class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def helper(jump, idx):
            if idx == n-1:
                return True

            jump1, jump2, jump3 = False, False, False
            for i in range(idx+1, n):
                gap = stones[i] - stones[idx]
                if stones[i] - stones[idx] > jump + 1:
                    break
                elif gap == jump - 1:
                    jump1 = helper(jump-1, i)
                elif gap == jump:
                    jump2 = helper(jump, i)
                elif gap == jump+1:
                    jump3 = helper(jump+1, i)
            return jump1 or jump2 or jump3

        # self.store = [None]*n
        n = len(stones)
        if stones[1] != 1:
            return False

        return helper(1, 1)
