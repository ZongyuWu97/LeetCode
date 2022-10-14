class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def backtrack(i):
            # 从下标i到结尾能否break
            if i == n:
                return True
            for j in range(i, n):
                # 下标i到j是否在wordDict
                if s[i:j+1] in wordDict:
                    if backtrack(j+1):
                        return True
            return False

        wordDict = set(wordDict)
        n = len(s)
        return backtrack(0)
