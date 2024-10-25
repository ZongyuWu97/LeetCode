class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(start, vertical):
            l = start
            r = len(matrix) - 1 if vertical else len(matrix[0]) - 1

            while l <= r:
                mid = (l + r) // 2
                if vertical:
                    if matrix[mid][start] < target:
                        l = mid + 1
                    elif matrix[mid][start] > target:
                        r = mid - 1
                    else:
                        return True
                else:
                    if matrix[start][mid] < target:
                        l = mid + 1
                    elif matrix[start][mid] > target:
                        r = mid - 1
                    else:
                        return True
            return False

        m, n = len(matrix), len(matrix[0])
        for i in range(min(m, n)):
            if binary(i, True) or binary(i, False):
                return True

        return False
