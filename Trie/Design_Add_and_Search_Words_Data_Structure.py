class WordDictionary:

    def __init__(self):
        self.Trie = {'$': False}
        self.maxLength = 0

    def addWord(self, word: str) -> None:
        node = self.Trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True
        self.maxLength = max(self.maxLength, len(word))

    def search(self, word: str) -> bool:
        def searchWord(word, node):
            for i, ch in enumerate(word):
                if ch in node:
                    node = node[ch]
                    continue

                if ch == '.':
                    for x in node:
                        if x != '$' and searchWord(word[i + 1:], node[x]):
                            return True
                return False
            return '$' in node

        if len(word) > self.maxLength:
            return False
        return searchWord(word, self.Trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
