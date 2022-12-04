class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        m, M = float('inf'), float('-inf')

        idx = 0
        for num in nums:
            if num < m:
                idx_m = idx
                m = num
            if num >= M:
                idx_M = idx
                M = num
            idx += 1

        if idx_m < idx_M:
            return idx_m + idx - 1 - idx_M
        elif idx_m == idx_M:
            return 0
        else:
            return idx_m + idx - 1 - idx_M - 1
