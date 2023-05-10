class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        memo = defaultdict(list)
        for idx, num in enumerate(nums):
            memo[num].append(idx)
        
        res = [0] * len(nums)
        for num in nums:
            curr = 0
            n = len(memo[num])
            pref = [0] * n
            for i in range(n):
                curr += memo[num][i]
                pref[i] = curr

            s = pref[-1]

            for idx, i in enumerate(memo[num]):
                res[i] += i * (idx * 2 - n + 2)
                res[i] += s - 2 * (pref[idx])
        return res