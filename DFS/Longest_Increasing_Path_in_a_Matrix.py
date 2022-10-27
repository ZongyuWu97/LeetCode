class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            # 返回从i，j开始的最长路径长度
            if path_length[i][j] != -1:
                return path_length[i][j]

            res = 0
            for dire in directions:
                new_position = (i+dire[0], j+dire[1])
                if 0 <= new_position[0] < m and 0 <= new_position[1] < n and\
                        matrix[new_position[0]][new_position[1]] > matrix[i][j]:
                    res = max(res, dfs(new_position[0], new_position[1]))

            path_length[i][j] = res+1
            return res+1

        m, n = len(matrix), len(matrix[0])
        path_length = [[-1]*n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if path_length[i][j] == -1:
                    dfs(i, j)

        return max(map(max, path_length))
