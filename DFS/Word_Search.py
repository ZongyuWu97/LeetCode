class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        self.found = False
        self.word = word
        self.board = board
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        wordLength = len(word)

        charBoard = defaultdict(int)
        for i in range(m):
            for j in range(n):
                charBoard[self.board[i][j]] += 1
        
        charWord = Counter(word)
        for char in charWord:
            if charWord[char] > charBoard[char]:
                return False
        
        for i in range(m):
            for j in range(n):
                    self.dfs(m, n, i, j, wordLength, 0, set([(i, j)]))
                    if self.found:
                        return True
        
        return False
    
    def dfs(self, m, n, i, j, wordLength, idx, visited):        
        if self.found or self.board[i][j] != self.word[idx]:
            return 
        if idx == wordLength - 1:
            self.found = True
            return 

        for direction in self.directions:
            new_row = i + direction[0]
            new_col = j + direction[1]

            if (new_row, new_col) in visited:
                continue
                
            if 0 <= new_row <= m - 1 and 0 <= new_col <= n - 1:
                visited.add((new_row, new_col))
                self.dfs( m, n, new_row, new_col, wordLength, idx + 1, visited)
                visited.remove((new_row, new_col))



