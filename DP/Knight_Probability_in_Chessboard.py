class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

        for move in range(1, k + 1):
            new_dp = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for m in moves:
                        new_r = r + m[0]
                        new_c = c + m[1]
                        if 0 <= new_r < n and 0 <= new_c < n:
                            new_dp[r][c] += dp[new_r][new_c] / 8.0
            dp = new_dp

        probability = 0.0
        for r in range(n):
            for c in range(n):
                probability += dp[r][c]

        return probability