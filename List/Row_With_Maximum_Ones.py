class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row_num, max_one = 0, 0
        for idx, row in enumerate(mat):
            new_sum = sum(row)
            if max_one < new_sum:
                max_one = new_sum
                row_num = idx
        return [row_num, max_one]