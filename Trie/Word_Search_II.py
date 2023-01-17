class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(row, col, parent):
            letter = board[row][col]
            node = parent[letter]

            word_match = node.pop('$', False)
            if word_match:
                res.append(word_match)

            board[row][col] = '.'
            for dire in directions:
                new_row = row + dire[0]
                new_col = col + dire[1]
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                if not board[new_row][new_col] in node:
                    continue

                backtrack(new_row, new_col, node)
            board[row][col] = letter

            if not node:
                parent.pop(letter)

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['$'] = word

        res = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(board), len(board[0])

        for row in range(m):
            for col in range(n):
                if board[row][col] in trie:
                    backtrack(row, col, trie)

        return res
