from collections import defaultdict


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        memo = defaultdict(int)
        count = 0
        m = len(target)
        for num in nums:
            n = len(num)
            if n >= m:
                continue

            count += memo[num]
            for i in range(n):
                if num[i] != target[i]:
                    break
            else:
                memo[target[n:]] += 1

            for i in range(n):
                if num[i] != target[-n + i]:
                    break
            else:
                memo[target[:-n]] += 1
        return count
