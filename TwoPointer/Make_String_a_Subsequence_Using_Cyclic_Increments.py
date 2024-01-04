class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def check(i, j):
            diff = (ord(str2[j]) - ord(str1[i])) % 26
            return diff == 0 or diff == 1

        m, n = len(str1), len(str2)
        if m < n:
            return False

        i, j = 0, 0
        while j < n:
            if i == m:
                return False
            while i < m:
                if check(i, j):
                    i += 1
                    j += 1
                    break
                else:
                    i += 1
        return True





        