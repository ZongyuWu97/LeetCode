class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        # satisfaction[:idx] < 0
        idx = bisect.bisect_left(satisfaction, 0)
        # increament of adding one negative number
        increament = sum(satisfaction[idx:])
        
        decreament = 0
        i = idx - 1
        while i >= 0:
            if decreament - satisfaction[i] < increament:
                decreament -= satisfaction[i]
                i -= 1
            else:
                break

        res = 0
        for j in range(n - i - 1):
            res += (j + 1) * satisfaction[i + 1 + j]
        
        return res