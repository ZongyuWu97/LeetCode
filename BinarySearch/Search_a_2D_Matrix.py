from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        first = []
        for i in range(m):
            first.append(matrix[i][0])
        

        rowIdx = max(bisect_left(first, target), 1)
        if target == first[min(rowIdx, m - 1)]:
            return True

        return target == matrix[rowIdx - 1][min(bisect_left(matrix[rowIdx - 1], target), n - 1)]

