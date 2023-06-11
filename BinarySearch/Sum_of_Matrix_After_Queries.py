from itertools import accumulate
from bisect import bisect_left

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows, cols = [(0, -1) for _ in range(n)], [(0, -1) for _ in range(n)]
        for order, (tp, idx, val) in enumerate(queries):
            if tp == 0:
                rows[idx] = (val, order)
            else:
                cols[idx] = (val, order)
        
        res = 0
        rows.sort(key=lambda x:x[1])
        row_order = [x[1] for x in rows]
        row_pref = list(accumulate([x[0] for x in rows]))
        
        for j in range(n):
            val, order = cols[j]
            idx = bisect_left(row_order, order)
            res += idx * val + row_pref[-1] - row_pref[idx - 1] * (idx > 0)

        return res