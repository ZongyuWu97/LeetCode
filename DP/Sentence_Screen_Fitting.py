class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)

        @lru_cache(None)
        def dp(i):  # return (nextIdx, times) when the i_th word is at the beginning of the row.
            c = 0
            times = 0
            while c + len(sentence[i]) <= cols:
                c += len(sentence[i]) + 1
                i += 1
                if i == n:
                    times += 1
                    i = 0
            return i, times

        ans = 0
        wordIdx = 0
        for _ in range(rows):
            ans += dp(wordIdx)[1]
            wordIdx = dp(wordIdx)[0]
        return ans