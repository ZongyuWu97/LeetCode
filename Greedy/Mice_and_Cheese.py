class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = []
        for i in range(n):
            diff.append((reward1[i] - reward2[i], i))
        diff.sort(reverse=True)
        res = 0
        for i in range(n):
            if k:
                res += reward1[diff[i][1]]
                k -= 1
            else:
                res += reward2[diff[i][1]]
        return res