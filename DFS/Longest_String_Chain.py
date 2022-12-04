class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.words = set(words)
        self.max_len = 0
        self.visited = set()
        for word in sorted(words, key=lambda x: -len(x)):
            if not word in self.visited:
                self.dfs(word, 1)
        return self.max_len

    def dfs(self, word, length):
        self.max_len = max(self.max_len, length)
        self.visited.add(word)
        n = len(word)
        for i in range(n):
            next_word = word[:i] + word[i + 1:]
            if next_word in self.words and not next_word in self.visited:
                self.dfs(next_word, length + 1)
