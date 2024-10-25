class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        # Max number of rows covered by k columns in matrix[:][:j]
        res = 0
        for cols in combinations(range(len(matrix[0])), numSelect):
            curr_covered = 0
            for row in matrix:
                for col, num in enumerate(row):
                    if num == 1 and not col in cols:
                        break
                else:
                    curr_covered += 1
            res = max(res, curr_covered)
        return res
