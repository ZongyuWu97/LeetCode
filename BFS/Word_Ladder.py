class Solution:
    from collections import defaultdict, deque

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        if beginWord == endWord:
            return 1

        n = len(beginWord)
        interWord = defaultdict(set)
        for word in wordList:
            for i in range(n):
                interWord[word[:i] + '.' + word[i + 1:]].add(word)
        wordList = set(wordList)

        q = deque()
        q.append([beginWord, 1])
        while q:
            curr, length = q.popleft()
            for i in range(n):
                inter = curr[:i] + '.' + curr[i + 1:]
                for nextWord in interWord[inter]:
                    if nextWord in wordList:
                        if nextWord == endWord:
                            return length + 1
                        else:
                            wordList.remove(nextWord)
                            q.append([nextWord, length + 1])

        return 0
