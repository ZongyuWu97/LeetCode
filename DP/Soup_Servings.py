class Solution:
    def soupServings(self, n: int) -> float:
        if n > 3500:
            return 1
        memo = {}
        def helper(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            if m <= 0 or n <= 0:
                return (m <= 0 and n > 0, m <= 0 and n <= 0)
            aFirst = (helper(m - 100, n)[0] + helper(m - 75, n - 25)[0]\
                + helper(m - 50, n - 50)[0] + helper(m - 25, n - 75)[0]) / 4
            aTogether = (helper(m - 100, n)[1] + helper(m - 75, n - 25)[1]\
                + helper(m - 50, n - 50)[1] + helper(m - 25, n - 75)[1]) / 4
            memo[(m, n)] = (aFirst, aTogether)
            return (aFirst, aTogether)
        
        prob = helper(n, n)
        return prob[0] + prob[1] * 0.5
            