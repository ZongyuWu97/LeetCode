from collections import Counter
from sortedcontainers import SortedSet
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        frequencyCount = Counter(count.values())
        res = 0
        s = SortedSet([-x for x in frequencyCount.keys()])


        while s:
            frequency = -s[0]
            res += frequencyCount[frequency] - 1
            s.discard(-frequency)
            if frequencyCount[frequency] > 1 and frequency > 1:
                s.add(-frequency + 1)
                frequencyCount[frequency - 1] += frequencyCount[frequency] - 1

        return res
            
            




