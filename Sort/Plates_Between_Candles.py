class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        def find_prev(l, r):
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if candles[mid] < l:
                    left = mid + 1
                else:
                    right = mid
            after_l = left

            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2 + 1
                if candles[mid] > r:
                    right = mid - 1
                else:
                    left = mid
            before_r = right
            return after_l, before_r

        candles = []
        n = len(s)
        for i in range(n):
            if s[i] == '|':
                candles.append(i)
        n = len(candles)

        ans = []
        for query in queries:
            after_l, before_r = find_prev(query[0], query[1])
            ans.append((candles[before_r] - candles[after_l] + 1) - (before_r - after_l + 1)
                       if after_l < before_r else 0)

        return ans
