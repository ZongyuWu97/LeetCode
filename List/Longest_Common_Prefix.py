class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        M = min([len(s) for s in strs])
        count = 0
        for i in range(M):
            new_count = count
            for s in strs:
                if s[i] != strs[0][i]:
                    break
            else:
                new_count += 1
            if count == new_count:
                break
            else:
                count = new_count
        return strs[0][:count]
