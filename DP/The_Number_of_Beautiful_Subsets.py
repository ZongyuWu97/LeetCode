class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        remainders = collections.defaultdict(dict)
        for num in nums:
            if num in remainders[num % k]:
                remainders[num % k][num] += 1
            else:
                remainders[num % k][num] = 1

        res = 1
        for r in remainders.values():
            # dp0 means don't take the current number, dp1 means take this number
            prev, dp0, dp1 = 0, 1, 0
            for num in sorted(r.keys()):
                frequency = r[num]
                v = pow(2, frequency)
                if prev + k == num:
                    dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)
                prev = num
            res *= dp0 + dp1
        return res - 1
