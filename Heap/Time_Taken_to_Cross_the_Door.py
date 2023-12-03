import heapq
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        curr = 0
        in_heap = []
        exit_heap = []
        idx = 0
        n = len(arrival)
        last = 1
        res = [0] * n

        while idx < n and (arrival[idx] >= curr or (not in_heap and not exit_heap)):
            if curr <= arrival[idx] - 1:
                last = 1
            curr = arrival[idx]
            while idx < n and arrival[idx] == curr:
                if state[idx]:
                    heapq.heappush(exit_heap, idx)
                else:
                    heapq.heappush(in_heap, idx)
                idx += 1
            # print(in_heap)
            # print(exit_heap)
            
            while (in_heap or exit_heap) and (idx == n or curr < arrival[idx]):
                if last:
                    if exit_heap:
                        res[heapq.heappop(exit_heap)] = curr
                    else:
                        last = 0
                        res[heapq.heappop(in_heap)] = curr
                else:
                    if in_heap:
                        res[heapq.heappop(in_heap)] = curr
                    else:
                        last = 1
                        res[heapq.heappop(exit_heap)] = curr
                curr += 1
            # print(res)
        return res


