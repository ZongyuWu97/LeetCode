from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for c in c1:
            if not c in c2 or c1[c] > c2[c]:
                return False
        return True
