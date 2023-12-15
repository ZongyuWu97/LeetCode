import heapq
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        res = 0
        for i in range(len(jobs)):
            res = max(res, math.ceil(jobs[i] / workers[i]))
        return res
