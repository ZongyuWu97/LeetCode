class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = collections.Counter(s)
        impossible = set([x for x in count if count[x] < k])
        n = len(s)

        ans = 0
        for currUnique in range(1, len(count) + 1):
            countMap = [0] * 26
            l, r = 0, 0
            windowUnique = 0
            chAtLeastK = 0
            while r < n:
                if s[r] in impossible:
                    l = r = r + 1
                    windowUnique = 0
                    chAtLeastK = 0
                    countMap = [0] * 26
                    if r == n:
                        break

                if windowUnique <= currUnique:
                    idx = ord(s[r]) - ord('a')
                    if countMap[idx] == 0:
                        windowUnique += 1
                    countMap[idx] += 1
                    if countMap[idx] == k:
                        chAtLeastK += 1
                    r += 1
                else:
                    idx = ord(s[l]) - ord('a')
                    if countMap[idx] == k:
                        chAtLeastK -= 1
                    countMap[idx] -= 1
                    if countMap[idx] == 0:
                        windowUnique -= 1
                    l += 1
                
                if currUnique == windowUnique == chAtLeastK:
                    ans = max(ans, r - l)
        return ans



                