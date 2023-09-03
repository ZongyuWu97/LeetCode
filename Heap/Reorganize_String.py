from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = [(-count[ch], ch) for ch in count]
        heapq.heapify(h)

        res = ['.']
        while h:
            first = heapq.heappop(h)
            if first[1] != res[-1]:
                res.append(first[1])
                if first[0] != -1:
                    heapq.heappush(h, (first[0] + 1, first[1]))
            elif h:
                second = heapq.heappop(h)
                res.append(second[1])
                if second[0] != -1:
                    heapq.heappush(h, (second[0] + 1, second[1]))
                heapq.heappush(h, first)
            else:
                return ''
        return ''.join(res[1:])
