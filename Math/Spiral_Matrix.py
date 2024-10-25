class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        count = 0
        ans = []
        i, j = 0, 0
        while count < m * n:
            ans.append(matrix[i][j])
            visited.add((i, j))
            count += 1
            new_i = i + directions[d][0]
            new_j = j + directions[d][1]
            if (
                new_i == -1
                or new_i == m
                or new_j == -1
                or new_j == n
                or (new_i, new_j) in visited
            ):
                d = (d + 1) % 4
                new_i = i + directions[d][0]
                new_j = j + directions[d][1]
            i, j = new_i, new_j

        return ans
