class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        memo = defaultdict(int)
        for num in nums:
            _, remainder = divmod(num, value)
            memo[remainder] += 1

        q = 0
        # print(memo)
        ok = 1
        while ok:
            i = 0
            while i < value:
                # print(i, memo[i])
                if memo[i]:
                    memo[i] -= 1
                    i += 1
                    continue
                ok = 0
                break
            if ok:
                q += 1
        return q * value + i
