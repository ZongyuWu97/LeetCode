from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        task = sorted(count.keys(), key=lambda x: -count[x])
        idle = (count[task[0]] - 1) * n

        ans = count[task[0]]
        for t in task[1:]:
            ans += count[t]
            idle = max(0, idle - min(count[task[0]] - 1, count[t]))
        ans += idle
        return ans
