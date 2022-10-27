class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(word):
            if word in memo:
                return memo[word]

            memo[word] = False
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in words or dfs(prefix)) and (suffix in words or dfs(suffix)):
                    memo[word] = True
                    return True
            return False

        words = set(words)
        res = []
        memo = {}
        for word in words:
            if dfs(word):
                res.append(word)
        return res
