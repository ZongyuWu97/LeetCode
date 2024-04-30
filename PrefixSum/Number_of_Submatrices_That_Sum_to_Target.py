from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                memo[i][j] = (
                    matrix[i - 1][j - 1]
                    + memo[i - 1][j]
                    + memo[i][j - 1]
                    - memo[i - 1][j - 1]
                )

        cnt = 0
        for x1 in range(1, m + 1):
            for x2 in range(x1, m + 1):
                dic = defaultdict(int)
                dic[0] = 1
                for y1 in range(1, n + 1):
                    tmp = memo[x2][y1] - memo[x1 - 1][y1]
                    cnt += dic[tmp - target]
                    dic[tmp] += 1

        return cnt
