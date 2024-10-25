class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            std = "".join(sorted(list(s)))
            if std in memo:
                memo[std].append(s)
            else:
                memo[std] = [s]
        return memo.values()
