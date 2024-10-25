class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)

                if num in cols[j]:
                    return False
                else:
                    cols[j].add(num)

                if num in blocks[i // 3 * 3 + j // 3]:
                    return False
                else:
                    blocks[i // 3 * 3 + j // 3].add(num)
        return True
