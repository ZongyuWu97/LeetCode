class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = []
        k = 0
        for i in range(min(m, n)):
            res.append(word1[i])
            res.append(word2[i])
            
        if m > n:
            return ''.join(res) + word1[n:]
        else:
            return ''.join(res) + word2[m:]
