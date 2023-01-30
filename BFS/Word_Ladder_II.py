class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        n = len(wordList[0])
        wordList = set(wordList)
        if not endWord in wordList:
            return []
        if beginWord == endWord:
            return [[beginWord]]

        # Build intermidiate words dictionary
        interWord = defaultdict(set)
        for word in wordList:
            for i in range(n):
                interWord[word[:i] + '.' + word[i + 1:]].add(word)

        # BFS for endWord
        q = deque()
        q.append([1, beginWord])
        visited = set([beginWord])
        level = defaultdict(set)
        level[1].add(beginWord)
        res = []
        while q:
            path = q.popleft()
            pre = path[-1]

            # Check if arrive at endWord
            if pre == endWord:
                length = path[0]
                res.append(path[1:])
                while q and q[0][0] == length:
                    path = q.popleft()
                    if path[-1] == endWord:
                        res.append(path[1:])
                break

            path[0] += 1
            for i in range(n):
                inter = pre[:i] + '.' + pre[i + 1:]

                for nextWord in interWord[inter]:
                    if not nextWord in visited or (nextWord in visited and nextWord in level[path[0]]):
                        visited.add(nextWord)
                        level[path[0]].add(nextWord)
                        q.append(path + [nextWord])

        return res
