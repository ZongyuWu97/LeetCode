class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [["."] * 3 for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            if i % 2:
                grid[r][c] = "O"
            else:
                grid[r][c] = "X"

        winner = "."
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != ".":
                winner = grid[i][0]
                break
            if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != ".":
                winner = grid[0][i]
                break
        else:
            if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ".":
                winner = grid[0][0]
            if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ".":
                winner = grid[0][2]

        if winner == "X":
            return "A"
        elif winner == "O":
            return "B"
        else:
            return "Draw" if len(moves) == 9 else "Pending"
