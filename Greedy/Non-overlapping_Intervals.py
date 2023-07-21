class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1]))
        store = None
        res = 0
        for interval in intervals:
            # print(store)
            if not store:
                store = interval
                continue
            if interval[0] == store[0]:
                res += 1
                continue
            if store[1] <= interval[0]:
                store = interval
                continue
            if store[1] <= interval[1]:
                res += 1
                continue
            res += 1
            store = interval
        return res