class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        memo = [0] * 2000

        res = 0
        for start, end, duration in tasks:
            while start <= end:
                if memo[start - 1]:
                    duration -= 1
                start += 1

            while duration > 0:
                if not memo[end - 1]:
                    memo[end - 1] = 1
                    res += 1
                    duration -= 1
                end -= 1
        return res
