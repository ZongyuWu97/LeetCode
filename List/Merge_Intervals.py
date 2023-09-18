class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in sorted(intervals, key = lambda i: i[0]):
            if ans and i[0] <= ans[-1][1]: ans[-1][1] = max(i[1], ans[-1][1])
            else: ans.append(i)
        return ans